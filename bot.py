import telebot
from config import TG_TOKEN
from telebot import types
from MedicalSurvey import MedicalSurvey
from QuestionsHandlers import Questions, QuestionsNumber, question_handlers
from datetime import datetime
from DatabaseManager import add_medical_survey, get_medical_survey
bot = telebot.TeleBot(TG_TOKEN)


def ask_question(message, survey, question):
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


def handle_question(q, survey, message):
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
        attr_name = f"Q{number - 1}"
        question = getattr(Questions, attr_name).value[0][0]
        ask_question(message, survey, question)
    elif question == "start":
        start(message)
    else:
        ask_question(message, survey, question)


def save_answer(survey, message, question):
    for q in QuestionsNumber:
        if question.startswith(q.value):
            handle_question(q, survey, message)
            break


def get_keyboard(question):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    for member in Questions.__members__.values():
        if member.value[0][0] == question:
            if member.value[0][1] is not None:
                count = 0
                for i in member.value[0]:
                    count += 1
                if count == 3 or count == 6:
                    for i in range(1, count):
                        keyboard.add(types.KeyboardButton(text=member.value[0][i]))

    else:
        keyboard.add(types.InlineKeyboardButton(text="назад", callback_data="back"))
    return keyboard


def finish_registration(survey, message):
    # Вывод всех данных
    survey.print_fields()
    add_medical_survey(survey)
    bot.send_message(message.chat.id, "Ваши данные успешно сохранены:\n")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Пожалуйста, введите номер вашего полиса:")
    bot.register_next_step_handler(message, process_policy_number)


def process_policy_number(message):
    policy_number = message.text
    survey = MedicalSurvey(policy_number)
    bot.send_message(message.chat.id, f"Спасибо! Ваш номер полиса: {policy_number}")
    bot.send_message(message.chat.id, "Привет! Для заполнения анкеты, пожалуйста, ответьте на следующие вопросы:")
    ask_question(message, survey, f"1. Дата анкетирования (день-месяц-год):", True, True)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id,
                     "Простите, я вас не понимаю. Если вы хотите заполнить анкету, то пропишите команду /start")


bot.polling()
