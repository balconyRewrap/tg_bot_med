from enum import Enum
from datetime import datetime


class Questions(Enum):
    # Начало главной информации
    Q1 = ("1. Дата анкетирования (день-месяц-год):", "Да", "Нет"),
    Q1_1 = ("1_1. Введите дату анкетирования. Формат день-месяц-год, например, 01-12-2023", None),
    Q2 = ("2. Ф.И.О. пациента:", None),
    Q3 = ("3. Пол (Муж или Жен):", None),
    Q4 = ("4. Дата рождения. Формат день-месяц-год, например, 01-12-2023:", None),
    Q5 = ("5. Вам полных лет:", "Да", "Нет"),
    Q5_1 = ("5_1. Введите число вам полных лет:", None),
    Q6 = ("6. Медицинская организация:", None),
    Q7 = (
        "7. Должность и Ф.И.О. медицинского работника, проводящего анкетирование и подготовку заключения по его "
        "результатам:", None),
    # Конец главной информации

    # Начало conditions
    Q8 = (
        "8. Говорил ли Вам врач когда-либо, что у Вас имеется гипертоническая болезнь (повышенное артериальное "
        "давление)?", "Да", "Нет"),
    Q8_1 = ("8_1. Если «Да», то принимаете ли Вы препараты для снижения давления?", "Да", "Нет"),
    Q9 = ("9. Имеется ли у вас ишемическая болезнь сердца (стенокардия)?", "Да", "Нет"),
    Q10 = ("10. Имеется ли у вас цереброваскулярное заболевание (заболевание сосудов головного мозга)?", "Да", "Нет"),
    Q11 = (
        "11. Имеется ли у вас хроническое заболевание бронхов или легких (хронический бронхит, эмфизема, бронхиальная "
        "астма)?",
        "Да", "Нет"),
    Q12 = ("12. Имеется ли у вас туберкулез (легких или иных локализаций)?", "Да", "Нет"),
    Q13 = ("13. Имеется ли у вас сахарный диабет или повышенный уровень сахара в крови?", "Да", "Нет"),
    Q13_1 = ("13_1. Если «Да», то принимаете ли Вы препараты для снижения уровня сахара?", "Да", "Нет"),
    Q14 = ("14. Имеются ли у вас заболевания желудка (гастрит, язвенная болезнь)?", "Да", "Нет"),
    Q15 = ("15. Имеется ли у вас хроническое заболевание почек?", "Да", "Нет"),
    Q16 = ("16. Имеется ли у вас злокачественное новообразование?", "Да", "Нет"),
    Q16_1 = ("16_1. Если «Да», то какое?", None),
    Q17 = ("17. Имеется ли у вас повышенный уровень холестерина?", "Да", "Нет"),
    Q17_1 = ("17_1. Если «Да», то принимаете ли Вы препараты для снижения уровня холестерина?", "Да", "Нет"),
    # Конец conditions главной информации

    # Начало Health_event
    Q18 = ("18. Был ли у Вас инфаркт миокарда?", "Да", "Нет"),
    Q19 = ("19. Был ли у Вас инсульт?", "Да", "Нет"),
    # Конец Health_event

    # Начало symptoms
    Q20 = (
        "20. Был ли инфаркт миокарда или инсульт у Ваших близких родственников в молодом или среднем возрасте (до 65 "
        "лет у матери или родных сестер или до 55 лет у отца или родных братьев)?",
        "Да", "Нет"),
    Q21 = (
        "21. Были ли у Ваших близких родственников в молодом или среднем возрасте злокачественные новообразования ("
        "легкого, желудка, кишечника, толстой или прямой кишки, предстательной железы, молочной железы, матки, "
        "опухоли других локализаций) или полипоз желудка, семейный аденоматоз/диффузный полипоз толстой кишки?",
        "Да", "Нет"),
    Q21_1 = (
        "21_1. Напишите, какое конкретно злокачественное новообразование у ваших близких родственников было:"
        "легкого, желудка, кишечника, толстой или прямой кишки, предстательной железы, молочной железы, матки, "
        "опухоли других локализаций) или полипоз желудка, семейный аденоматоз/диффузный полипоз толстой кишки? (",
        None),
    Q22 = (
        "22. Возникает ли у Вас, когда поднимаетесь по лестнице, идете в гору или спешите, или при выходе из теплого "
        "помещения на холодный воздух, боль или ощущение давления, жжения, тяжести или явного дискомфорта за грудиной "
        "и (или) в левой половине грудной клетки, и (или) в левом плече, и (или) в левой руке?",
        "Да", "Нет"),
    Q22_1 = (
        "22_1. Указанные боли/ощущения/дискомфорт исчезают сразу или в течение не более "
        "чем 20 мин после прекращения ходьбы/адаптации к холоду/ в тепле/в покое и (или) они исчезают через 1-5 мин "
        "после приема нитроглицерина",
        "Да", "Нет"),
    Q23 = (
        "23. Возникала ли у Вас когда-либо внезапная кратковременная слабость или неловкость при движении в одной "
        "руке (ноге) либо руке и ноге одновременно так, что Вы не могли взять или удержать предмет, встать со стула, "
        "пройтись по комнате?",
        "Да", "Нет"),
    Q24 = (
        "24. Возникало ли у Вас когда-либо внезапное без явных причин кратковременное онемение в одной руке, "
        "ноге или половине лица, губы или языка?",
        "Да", "Нет"),
    Q25 = ("25. Возникала ли у Вас когда-либо внезапно кратковременная потеря зрения на один глаз?", "Да", "Нет"),
    Q26 = (
        "26. Бывают ли у Вас ежегодно периоды ежедневного кашля с отделением мокроты на протяжении примерно 3-х месяцев"
        " в году?",
        "Да", "Нет"),
    Q27 = (
        "27. Бывают ли у Вас свистящие или жужжащие хрипы в грудной клетке "
        "при дыхании, не проходящие при откашливании?",
        "Да", "Нет"),
    Q28 = ("28. Бывало ли у Вас когда-либо кровохарканье?", "Да", "Нет"),
    Q29 = (
        "29. Беспокоят ли Вас боли в области верхней части живота (в области желудка), отрыжка, тошнота, рвота, "
        "ухудшение или отсутствие аппетита?",
        "Да", "Нет"),
    Q30 = ("30. Бывает ли у Вас неоформленный (полужидкий) черный или дегтеобразный стул?", "Да", "Нет"),
    Q31 = ("31. Похудели ли Вы за последнее время без видимых причин (т.е. без соблюдения диеты или увеличения "
           "физической активности и пр.)?", "Да", "Нет"),
    Q32 = ("32. Бывает ли у Вас боль в области заднепроходного отверстия?", "Да", "Нет"),
    Q33 = ("33. Бывают ли у Вас кровяные выделения с калом?", "Да", "Нет"),
    # Конец symptoms

    # Начало lifestyle
    Q34 = ("34. Курите ли Вы? (курение одной и более сигарет в день)", "Да", "Нет"),
    Q34_1 = ("34_1. Сколько в среднем сигарет в день выкуриваете?", None),
    Q35 = ("35. Сколько минут в день Вы тратите на ходьбу в умеренном или быстром темпе (включая дорогу до места "
           "работы и обратно)?", "До 30 минут", "30 минут и более"),
    Q36 = ("36. Присутствует ли в Вашем ежедневном рационе 400-500 г сырых овощей и фруктов?", "Да", "Нет"),
    Q37 = ("37. Имеете ли Вы привычку подсаливать приготовленную пищу, не пробуя ее?", "Да", "Нет"),
    Q38 = (
        "38. Принимали ли Вы за последний год психотропные или наркотические вещества без назначения врача?", "Да",
        "Нет"),
    Q39 = ("39. Как часто Вы употребляете алкогольные напитки?", "Никогда (0 баллов)", "Раз в месяц и реже (1 балл)",
           "2-4 раза в месяц (2 балла)", "2-3 раза в неделю (3 балла)", "≥ 4 раз в неделю (4 балла)"),
    Q40 = (
        "40. Какое количество алкогольных напитков (сколько порций) вы выпиваете обычно за один раз? 1 порция равна "
        "12 мл чистого этанола ИЛИ 30 мл крепкого алкоголя (водки) ИЛИ 100 мл сухого вина ИЛИ 300 мл пива",
        "1-2 порции (0 баллов)", "3-4 порции (1 балл)", "5-6 порций (2 балла)", "7-9 порций (3 балла)",
        "≥ 10 порций (4 балла)"),
    Q41 = (
        "41. Как часто Вы употребляете за один раз 6 или более порций? 6 порций равны ИЛИ 180 мл крепкого алкоголя ("
        "водки) ИЛИ 600 мл сухого вина ИЛИ 1,8 л пива",
        "Никогда (0 баллов)", "Раз в месяц и реже (1 балл)", "2-4 раза в месяц (2 балла)",
        "2-3 раза в неделю (3 балла)",
        "≥ 4 раз в неделю (4 балла)"),
    # Конец lifestyle

    # Начало additional_complaints
    Q42 = ("42. Есть ли у Вас другие жалобы на свое здоровье, не вошедшие в настоящую анкету и которые Вы бы хотели "
           "сообщить врачу (фельдшеру)", "Да", "Нет"),
    # Конец additional_complaints


class QuestionsNumber(Enum):
    Q1 = "1."
    Q1_1 = "1_1."
    Q2 = "2."
    Q3 = "3."
    Q4 = "4."
    Q5 = "5."
    Q5_1 = "5_1."
    Q6 = "6."
    Q7 = "7."
    Q8 = "8."
    Q8_1 = "8_1."
    Q9 = "9."
    Q10 = "10."
    Q11 = "11."
    Q12 = "12."
    Q13 = "13."
    Q13_1 = "13_1."
    Q14 = "14."
    Q15 = "15."
    Q16 = "16."
    Q16_1 = "16_1."
    Q17 = "17."
    Q17_1 = "17_1."
    Q18 = "18."
    Q19 = "19."
    Q20 = "20."
    Q21 = "21."
    Q21_1 = "21_1."
    Q22 = "22."
    Q22_1 = "22_1."
    Q23 = "23."
    Q24 = "24."
    Q25 = "25."
    Q26 = "26."
    Q27 = "27."
    Q28 = "28."
    Q29 = "29."
    Q30 = "30."
    Q31 = "31."
    Q32 = "32."
    Q33 = "33."
    Q34 = "34."
    Q34_1 = "34_1."
    Q35 = "35."
    Q36 = "36."
    Q37 = "37."
    Q38 = "38."
    Q39 = "39."
    Q40 = "40."
    Q41 = "41."
    Q42 = "42."


def handle_commands(message_text: str, question: int):
    if message_text == "/start":
        return "start", question
    elif message_text == "назад":
        return "назад", question
    elif message_text == "/get":
        return "get", question
    else:
        return "нет", question


def handle_q1(survey, message):
    msg, num = handle_commands(message.text, 1)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d-%m-%Y")
        survey.survey_date = formatted_date
        return Questions.Q2.value[0][0], 1
    elif additional_info == "Нет":
        survey.gender = message.text
        return Questions.Q1_1.value[0][0], 1
    else:
        return "Неверный выбор", 1


def handle_q1_1(survey, message):
    msg, num = handle_commands(message.text, 1)
    if not (msg == "нет"):
        return msg, num
    try:
        date = datetime.strptime(message.text, "%d-%m-%Y")
        survey.survey_date = date.strftime("%d-%m-%Y")
        return Questions.Q2.value[0][0], 1
    except ValueError:
        return "Неправильная Дата Анкетирования", 1


def handle_q2(survey, message):
    msg, num = handle_commands(message.text, 2)
    if not (msg == "нет"):
        return msg, num
    survey.patient_name = message.text

    return Questions.Q3.value[0][0], 2


def handle_q3(survey, message):
    msg, num = handle_commands(message.text, 3)
    if not (msg == "нет"):
        return msg, num
    if message.text == "Муж" or message.text == "Жен":
        survey.gender = message.text
        return Questions.Q4.value[0][0], 3
    else:
        return "Неправильный пол", 3


def handle_q4(survey, message):
    msg, num = handle_commands(message.text, 4)
    if not (msg == "нет"):
        return msg, num
    try:
        date = datetime.strptime(message.text, "%d-%m-%Y")
        survey.birth_date = date.strftime("%d-%m-%Y")
        
        survey_date = datetime.strptime(survey.survey_date, "%d-%m-%Y")

        age = survey_date.year - date.year
        if (date.month, survey_date.day) < (date.month, survey_date.day):
            age -= 1
        survey.age = age
        return Questions.Q5.value[0][0], 4
    except ValueError:
        return "Неправильная Дата Рождения", 4


def handle_q5(survey, message):
    msg, num = handle_commands(message.text, 5)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        return Questions.Q6.value[0][0], 5
    elif additional_info == "Нет":
        return Questions.Q5_1.value[0][0], 5
    else:
        return "Неверный выбор", 5


def handle_q5_1(survey, message):
    handle_commands(message.text, 1)
    try:
        survey.age = int(message.text)
        return Questions.Q6.value[0][0], 5
    except ValueError:
        return "Неправильное число", 5


def handle_q6(survey, message):
    msg, num = handle_commands(message.text, 6)
    if not (msg == "нет"):
        return msg, num
    survey.medical_organization = message.text
    return Questions.Q7.value[0][0], 6


def handle_q7(survey, message):
    msg, num = handle_commands(message.text, 7)
    if not (msg == "нет"):
        return msg, num
    survey.doctor_name = message.text
    return Questions.Q8.value[0][0], 7


def handle_q8(survey, message):
    msg, num = handle_commands(message.text, 8)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("hypertension", True)
        return Questions.Q8_1.value[0][0], 8
    elif additional_info == "Нет":
        survey.set_condition("hypertension", False)
        return Questions.Q9.value[0][0], 8
    else:
        return "Неверный выбор", 8


def handle_q8_1(survey, message):
    msg, num = handle_commands(message.text, 8)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("hypertension", True, True)
        return Questions.Q9.value[0][0], 8
    elif additional_info == "Нет":
        survey.set_condition("hypertension", True, False)
        return Questions.Q9.value[0][0], 8
    else:
        return "Неверный выбор", 8


def handle_q9(survey, message):
    msg, num = handle_commands(message.text, 9)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("ischemic_heart_disease", True)
        return Questions.Q10.value[0][0], 9
    elif additional_info == "Нет":
        survey.set_condition("ischemic_heart_disease", False)
        return Questions.Q10.value[0][0], 9
    else:
        return "Неверный выбор", 9


def handle_q10(survey, message):
    msg, num = handle_commands(message.text, 10)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("cerebrovascular_disease", True)
        return Questions.Q11.value[0][0], 10
    elif additional_info == "Нет":
        survey.set_condition("cerebrovascular_disease", False)
        return Questions.Q11.value[0][0], 10
    else:
        return "Неверный выбор", 10


def handle_q11(survey, message):
    msg, num = handle_commands(message.text, 11)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("chronic_lung_disease", True)
        return Questions.Q12.value[0][0], 11
    elif additional_info == "Нет":
        survey.set_condition("chronic_lung_disease", False)
        return Questions.Q12.value[0][0], 11
    else:
        return "Неверный выбор", 11


def handle_q12(survey, message):
    msg, num = handle_commands(message.text, 12)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("tuberculosis", True)
        return Questions.Q13.value[0][0], 12
    elif additional_info == "Нет":
        survey.set_condition("tuberculosis", False)
        return Questions.Q13.value[0][0], 12
    else:
        return "Неверный выбор", 12


def handle_q13(survey, message):
    msg, num = handle_commands(message.text, 13)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("diabetes", True)
        return Questions.Q13_1.value[0][0], 13
    elif additional_info == "Нет":
        survey.set_condition("diabetes", False)
        return Questions.Q14.value[0][0], 13
    else:
        return "Неверный выбор", 13


def handle_q13_1(survey, message):
    msg, num = handle_commands(message.text, 13)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("diabetes", True, True)
        return Questions.Q14.value[0][0], 13
    elif additional_info == "Нет":
        survey.set_condition("diabetes", True, False)
        return Questions.Q14.value[0][0], 13
    else:
        return "Неверный выбор", 13


def handle_q14(survey, message):
    msg, num = handle_commands(message.text, 14)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("stomach_disease", True)
        return Questions.Q15.value[0][0], 14
    elif additional_info == "Нет":
        survey.set_condition("stomach_disease", False)
        return Questions.Q15.value[0][0], 14
    else:
        return "Неверный выбор", 14


def handle_q15(survey, message):
    msg, num = handle_commands(message.text, 15)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("chronic_kidney_disease", True)
        return Questions.Q16.value[0][0], 15
    elif additional_info == "Нет":
        survey.set_condition("chronic_kidney_disease", False)
        return Questions.Q16.value[0][0], 15
    else:
        return "Неверный выбор", 15


def handle_q16(survey, message):
    msg, num = handle_commands(message.text, 16)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("cancer", True)
        return Questions.Q16_1.value[0][0], 16
    elif additional_info == "Нет":
        survey.set_condition("cancer", False)
        return Questions.Q17.value[0][0], 16
    else:
        return "Неверный выбор", 16


def handle_q16_1(survey, message):
    msg, num = handle_commands(message.text, 16)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    survey.set_condition("cancer", True, additional_info)
    return Questions.Q17.value[0][0], 16


def handle_q17(survey, message):
    msg, num = handle_commands(message.text, 17)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("high_cholesterol", True)
        return Questions.Q17_1.value[0][0], 17
    elif additional_info == "Нет":
        survey.set_condition("high_cholesterol", False)
        return Questions.Q18.value[0][0], 17
    else:
        return "Неверный выбор", 17


def handle_q17_1(survey, message):
    msg, num = handle_commands(message.text, 17)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_condition("high_cholesterol", True, True)
        return Questions.Q18.value[0][0], 17
    elif additional_info == "Нет":
        survey.set_condition("high_cholesterol", True, False)
        return Questions.Q18.value[0][0], 17
    else:
        return "Неверный выбор", 17


def handle_q18(survey, message):
    msg, num = handle_commands(message.text, 18)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_health_event("myocardial_infarction", True)
        return Questions.Q19.value[0][0], 18
    elif additional_info == "Нет":
        survey.set_health_event("myocardial_infarction", False)
        return Questions.Q19.value[0][0], 18
    else:
        return "Неверный выбор", 18


def handle_q19(survey, message):
    msg, num = handle_commands(message.text, 19)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_health_event("stroke", True)
        return Questions.Q20.value[0][0], 19
    elif additional_info == "Нет":
        survey.set_health_event("myocardial_infarction", False)
        return Questions.Q20.value[0][0], 19
    else:
        return "Неверный выбор", 19


def handle_q20(survey, message):
    msg, num = handle_commands(message.text, 20)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_family_history("heart_attack_or_stroke", True)
        return Questions.Q21.value[0][0], 20
    elif additional_info == "Нет":
        survey.set_family_history("heart_attack_or_stroke", False)
        return Questions.Q21.value[0][0], 20
    else:
        return "Неверный выбор", 20


def handle_q21(survey, message):
    msg, num = handle_commands(message.text, 21)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_family_history("cancer", True)
        return Questions.Q21_1.value[0][0], 21
    elif additional_info == "Нет":
        survey.set_family_history("cancer", False)
        return Questions.Q22.value[0][0], 21
    else:
        return "Неверный выбор", 21


def handle_q21_1(survey, message):
    msg, num = handle_commands(message.text, 21)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    survey.set_family_history("cancer", True, additional_info)
    return Questions.Q22.value[0][0], 21


def handle_q22(survey, message):
    msg, num = handle_commands(message.text, 22)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("chest_pain", True)
        return Questions.Q22_1.value[0][0], 22
    elif additional_info == "Нет":
        survey.set_symptom("chest_pain", False)
        return Questions.Q23.value[0][0], 22
    else:
        return "Неверный выбор", 22


def handle_q22_1(survey, message):
    msg, num = handle_commands(message.text, 22)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("chest_pain_disappears", True)
        return Questions.Q23.value[0][0], 22
    elif additional_info == "Нет":
        survey.set_symptom("chest_pain_disappears", False)
        return Questions.Q23.value[0][0], 22
    else:
        return "Неверный выбор", 22


def handle_q23(survey, message):
    msg, num = handle_commands(message.text, 23)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("sudden_weakness", True)
        return Questions.Q24.value[0][0], 23
    elif additional_info == "Нет":
        survey.set_symptom("sudden_weakness", False)
        return Questions.Q24.value[0][0], 23
    else:
        return "Неверный выбор", 23


def handle_q24(survey, message):
    msg, num = handle_commands(message.text, 24)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("sudden_numbness", True)
        return Questions.Q25.value[0][0], 24
    elif additional_info == "Нет":
        survey.set_symptom("sudden_numbness", False)
        return Questions.Q25.value[0][0], 24
    else:
        return "Неверный выбор", 24


def handle_q25(survey, message):
    msg, num = handle_commands(message.text, 25)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("sudden_vision_loss", True)
        return Questions.Q26.value[0][0], 25
    elif additional_info == "Нет":
        survey.set_symptom("sudden_vision_loss", False)
        return Questions.Q26.value[0][0], 25
    else:
        return "Неверный выбор", 25


def handle_q26(survey, message):
    msg, num = handle_commands(message.text, 26)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("chronic_cough", True)
        return Questions.Q27.value[0][0], 26
    elif additional_info == "Нет":
        survey.set_symptom("chronic_cough", False)
        return Questions.Q27.value[0][0], 26
    else:
        return "Неверный выбор", 26


def handle_q27(survey, message):
    msg, num = handle_commands(message.text, 27)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("wheezing", True)
        return Questions.Q28.value[0][0], 27
    elif additional_info == "Нет":
        survey.set_symptom("wheezing", False)
        return Questions.Q28.value[0][0], 27
    else:
        return "Неверный выбор", 27


def handle_q28(survey, message):
    msg, num = handle_commands(message.text, 28)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("coughing_blood", True)
        return Questions.Q29.value[0][0], 28
    elif additional_info == "Нет":
        survey.set_symptom("coughing_blood", False)
        return Questions.Q29.value[0][0], 28
    else:
        return "Неверный выбор", 28


def handle_q29(survey, message):
    msg, num = handle_commands(message.text, 29)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("upper_abdominal_pain", True)
        return Questions.Q30.value[0][0], 29
    elif additional_info == "Нет":
        survey.set_symptom("upper_abdominal_pain", False)
        return Questions.Q30.value[0][0], 29
    else:
        return "Неверный выбор", 29


def handle_q30(survey, message):
    msg, num = handle_commands(message.text, 30)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("black_stool", True)
        return Questions.Q31.value[0][0], 30
    elif additional_info == "Нет":
        survey.set_symptom("black_stool", False)
        return Questions.Q31.value[0][0], 30
    else:
        return "Неверный выбор", 30


def handle_q31(survey, message):
    msg, num = handle_commands(message.text, 31)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("unexplained_weight_loss", True)
        return Questions.Q32.value[0][0], 31
    elif additional_info == "Нет":
        survey.set_symptom("unexplained_weight_loss", False)
        return Questions.Q32.value[0][0], 31
    else:
        return "Неверный выбор", 31


def handle_q32(survey, message):
    msg, num = handle_commands(message.text, 32)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("anal_pain", True)
        return Questions.Q33.value[0][0], 32
    elif additional_info == "Нет":
        survey.set_symptom("anal_pain", False)
        return Questions.Q33.value[0][0], 32
    else:
        return "Неверный выбор", 32


def handle_q33(survey, message):
    msg, num = handle_commands(message.text, 33)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_symptom("blood_in_stool", True)
        return Questions.Q34.value[0][0], 33
    elif additional_info == "Нет":
        survey.set_symptom("blood_in_stool", False)
        return Questions.Q34.value[0][0], 33
    else:
        return "Неверный выбор", 33


def handle_q34(survey, message):
    msg, num = handle_commands(message.text, 34)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_lifestyle("smoking", True)
        return Questions.Q34_1.value[0][0], 34
    elif additional_info == "Нет":
        survey.set_symptom("smoking", False)
        return Questions.Q35.value[0][0], 34
    else:
        return "Неверный выбор", 34


def handle_q34_1(survey, message):
    msg, num = handle_commands(message.text, 34)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    try:
        additional_info = int(additional_info)
        survey.set_symptom("cigarettes_per_day", additional_info)
        return Questions.Q35.value[0][0], 34
    except ValueError:
        return "Неправильное число", 34


def handle_q35(survey, message):
    msg, num = handle_commands(message.text, 35)
    if not (msg == "нет"):
        return msg, num
    if message.text == "До 30 минут":
        survey.set_symptom("walking_minutes_per_day", 29)
        return Questions.Q36.value[0][0], 35
    elif message.text == "30 минут и более":
        survey.set_symptom("walking_minutes_per_day", 30)
        return Questions.Q36.value[0][0], 35
    else:
        return "Неверный выбор", 35


def handle_q36(survey, message):
    msg, num = handle_commands(message.text, 36)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_lifestyle("vegetable_fruit_intake", True)
    elif additional_info == "Нет":
        survey.set_symptom("vegetable_fruit_intake", False)
    else:
        return "Неверный выбор", 36
    return Questions.Q37.value[0][0], 36


def handle_q37(survey, message):
    msg, num = handle_commands(message.text, 37)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_lifestyle("salt_habit", True)
    elif additional_info == "Нет":
        survey.set_symptom("salt_habit", False)
    else:
        return "Неверный выбор", 37
    return Questions.Q38.value[0][0], 37


def handle_q38(survey, message):
    msg, num = handle_commands(message.text, 38)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_lifestyle("drug_use", True)
    elif additional_info == "Нет":
        survey.set_symptom("drug_use", False)
    else:
        return "Неверный выбор", 38
    return Questions.Q39.value[0][0], 38


def handle_q39(survey, message):
    msg, num = handle_commands(message.text, 39)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Никогда (0 баллов)":
        survey.set_lifestyle("alcohol_frequency", 0)
    elif additional_info == "Раз в месяц и реже (1 балл)":
        survey.set_lifestyle("alcohol_frequency", 1)
    elif additional_info == "2-4 раза в месяц (2 балла)":
        survey.set_lifestyle("alcohol_frequency", 2)
    elif additional_info == "2-3 раза в неделю (3 балла)":
        survey.set_lifestyle("alcohol_frequency", 3)
    elif additional_info == "≥ 4 раз в неделю (4 балла)":
        survey.set_lifestyle("alcohol_frequency", 4)
    else:
        return "Неверный выбор", 39
    return Questions.Q40.value[0][0], 39


def handle_q40(survey, message):
    msg, num = handle_commands(message.text, 40)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "1-2 порции (0 баллов)":
        survey.set_lifestyle("alcohol_portions", 0)
    elif additional_info == "3-4 порции (1 балл)":
        survey.set_lifestyle("alcohol_portions", 1)
    elif additional_info == "5-6 порций (2 балла)":
        survey.set_lifestyle("alcohol_portions", 2)
    elif additional_info == "7-9 порций (3 балла)":
        survey.set_lifestyle("alcohol_portions", 3)
    elif additional_info == "≥ 10 порций (4 балла)":
        survey.set_lifestyle("alcohol_portions", 4)
    else:
        return "Неверный выбор", 40
    return Questions.Q41.value[0][0], 40


def handle_q41(survey, message):
    msg, num = handle_commands(message.text, 41)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Никогда (0 баллов)":
        survey.set_lifestyle("binge_drinking_frequency", 0)
    elif additional_info == "Раз в месяц и реже (1 балл)":
        survey.set_lifestyle("binge_drinking_frequency", 1)
    elif additional_info == "2-4 раза в месяц (2 балла)":
        survey.set_lifestyle("binge_drinking_frequency", 2)
    elif additional_info == "2-3 раза в неделю (3 балла)":
        survey.set_lifestyle("binge_drinking_frequency", 3)
    elif additional_info == "≥ 4 раз в неделю (4 балла)":
        survey.set_lifestyle("binge_drinking_frequency", 4)
    else:
        return "Неверный выбор", 41
    survey.calculate_score()
    return Questions.Q42.value[0][0], 41


def handle_q42(survey, message):
    msg, num = handle_commands(message.text, 42)
    if not (msg == "нет"):
        return msg, num
    additional_info = message.text
    if additional_info == "Да":
        survey.set_additional_complaints(True)
        return "end", 42
    elif additional_info == "Нет":
        survey.set_additional_complaints(False)
        return "end", 42
    else:
        return "Неверный выбор", 42


question_handlers = {
    QuestionsNumber.Q1: handle_q1,
    QuestionsNumber.Q1_1: handle_q1_1,
    QuestionsNumber.Q2: handle_q2,
    QuestionsNumber.Q3: handle_q3,
    QuestionsNumber.Q4: handle_q4,
    QuestionsNumber.Q5: handle_q5,
    QuestionsNumber.Q5_1: handle_q5_1,
    QuestionsNumber.Q6: handle_q6,
    QuestionsNumber.Q7: handle_q7,
    QuestionsNumber.Q8: handle_q8,
    QuestionsNumber.Q8_1: handle_q8_1,
    QuestionsNumber.Q9: handle_q9,
    QuestionsNumber.Q10: handle_q10,
    QuestionsNumber.Q11: handle_q11,
    QuestionsNumber.Q12: handle_q12,
    QuestionsNumber.Q13: handle_q13,
    QuestionsNumber.Q13_1: handle_q13_1,
    QuestionsNumber.Q14: handle_q14,
    QuestionsNumber.Q15: handle_q15,
    QuestionsNumber.Q16: handle_q16,
    QuestionsNumber.Q16_1: handle_q16_1,
    QuestionsNumber.Q17: handle_q17,
    QuestionsNumber.Q17_1: handle_q17_1,
    QuestionsNumber.Q18: handle_q18,
    QuestionsNumber.Q19: handle_q19,
    QuestionsNumber.Q20: handle_q20,
    QuestionsNumber.Q21: handle_q21,
    QuestionsNumber.Q21_1: handle_q21_1,
    QuestionsNumber.Q22: handle_q22,
    QuestionsNumber.Q22_1: handle_q22_1,
    QuestionsNumber.Q23: handle_q23,
    QuestionsNumber.Q24: handle_q24,
    QuestionsNumber.Q25: handle_q25,
    QuestionsNumber.Q26: handle_q26,
    QuestionsNumber.Q27: handle_q27,
    QuestionsNumber.Q28: handle_q28,
    QuestionsNumber.Q29: handle_q29,
    QuestionsNumber.Q30: handle_q30,
    QuestionsNumber.Q31: handle_q31,
    QuestionsNumber.Q32: handle_q32,
    QuestionsNumber.Q33: handle_q33,
    QuestionsNumber.Q34: handle_q34,
    QuestionsNumber.Q34_1: handle_q34_1,
    QuestionsNumber.Q35: handle_q35,
    QuestionsNumber.Q36: handle_q36,
    QuestionsNumber.Q37: handle_q37,
    QuestionsNumber.Q38: handle_q38,
    QuestionsNumber.Q39: handle_q39,
    QuestionsNumber.Q40: handle_q40,
    QuestionsNumber.Q41: handle_q41,
    QuestionsNumber.Q42: handle_q42,
}
