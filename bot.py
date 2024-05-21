import telebot
from config import TG_TOKEN, BOT_PASSWORD
from telebot import types
from MedicalSurvey import MedicalSurvey
from QuestionsHandlers import Questions, QuestionsNumber, question_handlers
from datetime import datetime
from DatabaseManager import add_medical_survey, get_medical_survey
from typing import List
bot = telebot.TeleBot(TG_TOKEN)


def ask_question(message: telebot.types.Message, survey: MedicalSurvey, question: str):
    if question == Questions.Q1.value[0][0]:
        current_date = datetime.now()
        bot.send_message(message.chat.id, Questions.Q1.value[0][0])
        formatted_date = current_date.strftime("%d-%m-%Y")
        bot.send_message(message.chat.id, f"{formatted_date}")
        msg = bot.send_message(message.chat.id, "Все верно?", reply_markup=get_keyboard(Questions.Q1.value[0][0]))
        bot.register_next_step_handler(msg, lambda m: save_answer(survey, m, question))
    elif question == Questions.Q5.value[0][0]:
        msg = bot.send_message(message.chat.id, question, reply_markup=get_keyboard(Questions.Q1.value[0][0]))
        bot.send_message(message.chat.id, f"{survey.age}")
        bot.register_next_step_handler(msg, lambda m: save_answer(survey, m, question))
    else:
        msg = bot.send_message(message.chat.id, question, reply_markup=get_keyboard(question))
        bot.register_next_step_handler(msg, lambda m: save_answer(survey, m, question))


def handle_question(q: QuestionsNumber, survey: MedicalSurvey, message: telebot.types.Message):
    question, number = question_handlers[q](survey, message)
    if question == "end":
        finish_registration(survey, message)
    elif question == "Неправильная Дата Анкетирования":
        bot.send_message(message.chat.id, "Неправильно введена дата анкетирования")
        message.text = ""
        ask_question(message, survey, Questions.Q1_1.value[0][0])
    elif question == "Неправильная Дата Рождения":
        bot.send_message(message.chat.id, "Неправильно введена Дата Рождения")
        message.text = ""
        ask_question(message, survey, Questions.Q4.value[0][0])
    elif question == "Неправильное число" or question == "Неверный выбор" or question == "Неправильный пол":
        bot.send_message(message.chat.id, question)
        bot.send_message(message.chat.id, "Введите заново, пожалуйста:")
        message.text = ""
        attr_name = f"Q{number}"
        question = getattr(Questions, attr_name).value[0][0]
        ask_question(message, survey, question)
    elif question == "назад":
        bot.send_message(message.chat.id, "Вы вернулись на предыдущий шаг.")
        if number == 1:
            attr_name = f"Q{number}"
        else:
            attr_name = f"Q{number-1}"
        question = getattr(Questions, attr_name).value[0][0]
        ask_question(message, survey, question)
    elif question == "start":
        start(message)
    elif question == "get":
        get_survey(message)
    else:
        ask_question(message, survey, question)


def save_answer(survey: MedicalSurvey, message: telebot.types.Message, question: str) -> None:
    for q in QuestionsNumber:
        if question.startswith(q.value):
            handle_question(q, survey, message)
            break


def get_keyboard(question: str) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    for member in Questions.__members__.values():
        if member.value[0][0] == question:
            if member.value[0][1] is not None:
                count = 0
                for _ in member.value[0]:
                    count += 1
                if count == 3 or count == 6:
                    for i in range(1, count):
                        keyboard.add(types.KeyboardButton(text=member.value[0][i]))

    else:
        keyboard.add(types.InlineKeyboardButton(text="назад", callback_data="back"))
    return keyboard


def finish_registration(survey: MedicalSurvey, message: telebot.types.Message) -> None:
    # Вывод всех данных
    survey.print_fields()
    add_medical_survey(survey)
    bot.send_message(message.chat.id, "Ваши данные успешно сохранены:\n")


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message) -> None:
    bot.send_message(message.chat.id, "Пожалуйста, введите номер вашего полиса:", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, process_policy_number)


def process_policy_number(message: telebot.types.Message) -> None:
    if message.text is None:
        return
    if message.text.startswith("/get"):
        get_survey(message)
        return
    policy_number: str = message.text
    survey: MedicalSurvey = MedicalSurvey(policy_number)
    bot.send_message(message.chat.id, f"Спасибо! Ваш номер полиса: {policy_number}")
    bot.send_message(message.chat.id, "Привет! Для заполнения анкеты, пожалуйста, ответьте на следующие вопросы:")
    ask_question(message, survey, f"1. Дата анкетирования (день-месяц-год):")


@bot.message_handler(commands=['get'])
def get_survey(message: telebot.types.Message) -> None:
    if message.text is None:
        bot.send_message(message.chat.id, "Неправильный формат команды. Пожалуйста, "
                                          "введите команду в формате /get пароль номер_полиса")
        return
    
    command: List[str] = message.text.split()
    if len(command) != 3:
        bot.send_message(message.chat.id, "Неправильный формат команды. Пожалуйста, "
                                          "введите команду в формате /get пароль номер_полиса")
        return
    
    password: str = command[1]
    policy_number: str = command[2]
    
    # Проверка пароля
    if password != BOT_PASSWORD:
        bot.send_message(message.chat.id, "Неправильный пароль")
        return
    
    survey: MedicalSurvey | None = get_medical_survey(policy_number)
    if survey is None:
        bot.send_message(message.chat.id, "Анкета не найдена")
        return
    
    (formatted_data_main, formatted_data_conditions, formatted_data_health_events, formatted_data_family_history,
     formatted_data_symptoms, formatted_data_lifestyle,
     formatted_data_additional_complaints) = survey.format_data_as_html()
    
    bot.send_message(message.chat.id, formatted_data_main, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_conditions, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_health_events, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_family_history, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_symptoms, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_lifestyle, parse_mode='HTML')
    bot.send_message(message.chat.id, formatted_data_additional_complaints, parse_mode='HTML')



@bot.message_handler(func=lambda message: True)
def echo_all(message: telebot.types.Message) -> None:
    bot.send_message(message.chat.id,
                     "Простите, я вас не понимаю. Если вы хотите заполнить анкету, то пропишите команду /start")


bot.polling()
