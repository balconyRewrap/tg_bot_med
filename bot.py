import telebot
from telebot import types
from MedicalSurvey import MedicalSurvey
from QuestionsHandlers import Questions, QuestionsNumber, question_handlers

# Замените 'YOUR_TOKEN' на ваш токен, полученный от BotFather в Telegram
bot = telebot.TeleBot('6455505820:AAHPvsR9fDxWtO8Okg2yz_XBLBt41J3Jn44')


# Функция для запроса следующей переменной
def get_last_question_text(question):
    questions = list(Questions)
    index = 0
    for q in questions:
        if q.value[0][0] == question:
            break
        index += 1
    previous_question = questions[index - 1 - 1]
    return str(previous_question.value[0][0])


def ask_question(message, survey, question):
    if message.text == "назад":
        bot.send_message(message.chat.id, "Вы вернулись на предыдущий шаг.")
        question_text = get_last_question_text(question)
        message.text = ""
        ask_question(message, survey, question_text)
    else:
        msg = bot.send_message(message.chat.id, question, reply_markup=get_keyboard(question))
        bot.register_next_step_handler(msg, lambda m: save_answer(survey, m, question))


def handle_question(q, survey, message):
    question = question_handlers[q](survey, message)
    if question == "end":
        finish_registration(survey, message)
    ask_question(message, survey, question)


def save_answer(survey, message, question):
    for q in QuestionsNumber:
        if question.startswith(q.value):
            handle_question(q, survey, message)
            break


# Функция для создания клавиатуры с кнопками "Да" и "Нет"
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


# Функция для завершения регистрации и отправки данных
def finish_registration(survey, message):
    # Вывод всех данных
    survey.print_fields()
    bot.send_message(message.chat.id, "Ваши данные успешно сохранены:\n")


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    survey = MedicalSurvey()
    bot.send_message(message.chat.id, "Привет! Для заполнения анкеты, пожалуйста, ответьте на следующие вопросы:")
    ask_question(message, survey, "1. Дата анкетирования (день, месяц, год):")


# Обработчик для любого текстового ввода
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Простите, я вас не понимаю. Для начала заполните анкету.")


# Запуск бота
bot.polling()

