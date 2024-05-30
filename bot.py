import telebot
from telebot import types
from config import TG_TOKEN, TG_ADMINS_ID
from MedicalSurvey import MedicalSurvey
from QuestionsHandlers import get_first_question, get_next_question_by_id, Question, QuestionType, save_survey_date, handle_answer, get_question_by_id, get_next_question_id_by_id, get_last_question_by_id
from datetime import datetime
from DatabaseManager import add_medical_survey
bot = telebot.TeleBot(TG_TOKEN)
survey = MedicalSurvey("")

user_answers = {"user_id": 0, "answer_id": -1, "answer": ""}

def get_keyboard(question: Question) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    if question.has_options:
        for option in question.options:
            keyboard.add(types.KeyboardButton(text=option))
    keyboard.add(types.KeyboardButton(text="Назад"))
    return keyboard

# Функция для сохранения ответа пользователя
def save_answer(current_question_id: int, message) -> bool:
    global survey
    if current_question_id == 0:
        save_survey_date(survey)
    try:
        handle_answer(question_id=current_question_id,  survey=survey, message=message)
        pass
    except ValueError as e:
        question= get_question_by_id(current_question_id)
        if question:
            if question.question_type == QuestionType.DATE.value:
                bot.send_message(message.chat.id, "Неправильный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ")
            elif question.question_type == QuestionType.CHOICE.value:
                bot.send_message(message.chat.id, "Этого варианта нету в списке. Пожалуйста, выберите один из предложенных вариантов")
            elif current_question_id == 41:
                bot.send_message(message.chat.id, "Неправильный формат числа. Пожалуйста, введите число")
        return True
    return False

def change_user_state(next_question_id: int, message):
    user_answers["answer_id"] = next_question_id
    user_answers["answer"] = message.text



# Функция для отправки вопроса пользователю
def send_question(chat_id, question):
    formatted_date = ""
    if question.id == 1:
        current_date = datetime.now()
        formatted_date = " " + current_date.strftime("%d-%m-%Y")
    bot.send_message(chat_id, question.question_text + formatted_date, reply_markup=get_keyboard(question))

@bot.message_handler(commands=['start']) 
def start(message: telebot.types.Message) -> None:
    global user_answers 
    user_answers = {"user_id": message.chat.id, "answer_id": 0, "answer": ""}
    send_question(message.chat.id, get_first_question())

@bot.message_handler(func=lambda message: message.text == "Назад")
def back(message: telebot.types.Message) -> None:
    global user_answers 
    answer_id = user_answers["answer_id"]
    last_question = get_last_question_by_id(answer_id)
    if last_question:
        change_user_state(last_question.id, message)
        send_question(message.chat.id, last_question)

def finish_registration(survey: MedicalSurvey, message: telebot.types.Message) -> None:
    # Вывод всех данных
    survey.print_fields()
    add_medical_survey(survey)
    bot.send_message(message.chat.id, "Ваши данные успешно сохранены:\n")
    for id in TG_ADMINS_ID:
        bot.send_message(id, "Новая анкета заполнена:\n")
        (formatted_data_main, formatted_data_conditions, formatted_data_health_events, formatted_data_family_history,
        formatted_data_symptoms, formatted_data_lifestyle,
        formatted_data_additional_complaints) = survey.format_data_as_html()
        
        bot.send_message(id, formatted_data_main, parse_mode='HTML')
        bot.send_message(id, formatted_data_conditions, parse_mode='HTML')
        bot.send_message(id, formatted_data_health_events, parse_mode='HTML')
        bot.send_message(id, formatted_data_family_history, parse_mode='HTML')
        bot.send_message(id, formatted_data_symptoms, parse_mode='HTML')
        bot.send_message(id, formatted_data_lifestyle, parse_mode='HTML')
        bot.send_message(id, formatted_data_additional_complaints, parse_mode='HTML')


# Обработчик ответов от пользователя
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global survey
    global user_answers
    chat_id = message.chat.id
    answer_id = user_answers["answer_id"]
    if answer_id in range(0, 50):
        current_question_id = user_answers["answer_id"]
        next_question = get_next_question_by_id(current_question_id, message.text)
        next_question_id = get_next_question_id_by_id(answer = message.text, id = current_question_id)
        if next_question and next_question_id:
            has_error = save_answer(current_question_id, message)
            if has_error:
                current_question = get_question_by_id(current_question_id)
                change_user_state(current_question_id, message)
                send_question(chat_id, current_question)
            else:
                change_user_state(next_question_id, message)
                send_question(chat_id, next_question)
        else:
            has_error = save_answer(current_question_id, message)
            if has_error:
                current_question = get_question_by_id(current_question_id)
                change_user_state(current_question_id, message)
                send_question(chat_id, current_question)
            else:
                change_user_state(-1, message)
            bot.send_message(chat_id, "Спасибо за заполнение анкеты!")
            finish_registration(survey, message)
    else:
        bot.send_message(chat_id, "Чтобы начать анкету, введите /start")

bot.polling()




    




bot.polling()
