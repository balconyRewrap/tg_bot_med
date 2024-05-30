from enum import Enum
class Question():
    def __init__(self, id, question_text, question_type, has_options, options, next_question_id=None, previous_question_id=None, parent_question_id = None):
        self.id : int = id
        self.question_text: str = question_text
        self.question_type: str = question_type
        self.has_options: bool = has_options
        self.options: tuple[str] | None = options
        self.next_question_id: int | None = next_question_id
        self.previous_question_id: int | None = previous_question_id
        self.parent_question_id: int | None = parent_question_id

class QuestionType(Enum):
    TEXT = "String"
    DATE = "Date"
    CHOICE = "Choice"
    # Создание словаря вопросов
questions: dict[int, Question] = {
    0: Question(0, "Пожалуйста, введите номер вашего полиса:", "String", False, None, 1, None),
    1: Question(1, "1. Дата анкетирования (день-месяц-год):", "Choice", True, ("Да", "Нет"), 2, None),
    2: Question(2, "1_1. Введите дату анкетирования. Формат день-месяц-год, например, 01-12-2023", "Date", False, None, 3, 1, 1),
    3: Question(3, "2. Ф.И.О. пациента:", "String", False, None, 4, 2),
    4: Question(4, "3. Пол:", "Choice", True, ("Муж", "Жен"), 5, 3),
    5: Question(5, "4. Дата рождения. Формат день-месяц-год, например, 01-12-2023:", "Date", False, None, 6, 4),
    6: Question(6, "5. Медицинская организация:", "String", False, None, 7, 5),
    7: Question(7, "6. Должность и Ф.И.О. медицинского работника, проводящего анкетирование и подготовку заключения по его результатам:", "String", False, None, 8, 6),
    # Конец главной информации

    # Начало conditions
    8: Question(8, "7. Говорил ли Вам врач когда-либо, что у Вас имеется гипертоническая болезнь (повышенное артериальное давление)?", "Choice", True, ("Да", "Нет"), 9, 8),
    9: Question(9, "7_1. Если «Да», то принимаете ли Вы препараты для снижения давления?", "Choice", True, ("Да", "Нет"), 10, 8, 8),
    10: Question(10, "8. Имеется ли у вас ишемическая болезнь сердца (стенокардия)?", "Choice", True, ("Да", "Нет"), 11, 9),
    11: Question(11, "9. Имеется ли у вас цереброваскулярное заболевание (заболевание сосудов головного мозга)?", "Choice", True, ("Да", "Нет"), 12, 10),
    12: Question(12, "10. Имеется ли у вас хроническое заболевание бронхов или легких (хронический бронхит, эмфизема, бронхиальная астма)?", "Choice", True, ("Да", "Нет"), 13, 11),
    13: Question(13, "11. Имеется ли у вас туберкулез (легких или иных локализаций)?", "Choice", True, ("Да", "Нет"), 14, 12),
    14: Question(14, "12. Имеется ли у вас сахарный диабет или повышенный уровень сахара в крови?", "Choice", True, ("Да", "Нет"), 15, 13),
    15: Question(15, "12_1. Если «Да», то принимаете ли Вы препараты для снижения уровня сахара?", "Choice", True, ("Да", "Нет"), 16, 14, 14),
    16: Question(16, "13. Имеются ли у вас заболевания желудка (гастрит, язвенная болезнь)?", "Choice", True, ("Да", "Нет"), 17, 14),
    17: Question(17, "14. Имеется ли у вас хроническое заболевание почек?", "Choice", True, ("Да", "Нет"), 18, 16),
    18: Question(18, "15. Имеется ли у вас злокачественное новообразование?", "Choice", True, ("Да", "Нет"), 19, 17),
    19: Question(19, "15_1. Если «Да», то какое?", "String", False, None, 20, 18, 18),
    20: Question(20, "16. Имеется ли у вас повышенный уровень холестерина?", "Choice", True, ("Да", "Нет"), 21, 18),
    21: Question(21, "16_1. Если «Да», то принимаете ли Вы препараты для снижения уровня холестерина?", "Choice", True, ("Да", "Нет"), 22, 20, 20),

    # Конец conditions главной информации

    # Начало Health_event
    22: Question(22, "17. Был ли у Вас инфаркт миокарда?", "Choice", True, ("Да", "Нет"), 23, 21),
    23: Question(23, "18. Был ли у Вас инсульт?", "Choice", True, ("Да", "Нет"), 24, 22),
    # Конец Health_event

    # Начало family_history
    24: Question(24, "19. Был ли инфаркт миокарда или инсульт у Ваших близких родственников в молодом или среднем возрасте (до 65 лет у матери или родных сестер или до 55 лет у отца или родных братьев)?", "Choice", True, ("Да", "Нет"), 25, 23),
    25: Question(25, "20. Были ли у Ваших близких родственников в молодом или среднем возрасте злокачественные новообразования (легкого, желудка, кишечника, толстой или прямой кишки, предстательной железы, молочной железы, матки, опухоли других локализаций) или полипоз желудка, семейный аденоматоз/диффузный полипоз толстой кишки?", "Choice", True, ("Да", "Нет"), 26, 24),
    26: Question(26, "20_1. Напишите, какое конкретно злокачественное новообразование у ваших близких родственников было: легкого, желудка, кишечника, толстой или прямой кишки, предстательной железы, молочной железы, матки, опухоли других локализаций) или полипоз желудка, семейный аденоматоз/диффузный полипоз толстой кишки?", "String", False, None, 27, 25, 25),
    # Конец family_history

    # Начало symptoms
    27: Question(27, "21. Возникает ли у Вас, когда поднимаетесь по лестнице, идете в гору или спешите, или при выходе из теплого "
            "помещения на холодный воздух, боль или ощущение давления, жжения, тяжести или явного дискомфорта за грудиной "
            "и (или) в левой половине грудной клетки, и (или) в левом плече, и (или) в левой руке?", "Choice", True, ("Да", "Нет"), 28, 25),
    28: Question(28, "21_1. Указанные боли/ощущения исчезают сразу или в течение не более чем 20 мин после прекращения ходьбы/адаптации к холоду/ в тепле/в покое и (или) они исчезают через 1-5 мин после приема нитроглицерина", "Choice", True, ("Да", "Нет"), 29, 27, 27),
    29: Question(29, "22. Возникала ли у Вас когда-либо внезапная кратковременная слабость или неловкость при движении в одной " 
                "руке (ноге) либо руке и ноге одновременно так, что Вы не могли взять или удержать предмет, встать со стула, " 
                "пройтись по комнате?", "Choice", True, ("Да", "Нет"), 30, 28),
    30: Question(30, "23. Возникало ли у Вас когда-либо внезапное без явных причин кратковременное онемение в одной руке, "
                "ноге или половине лица, губы или языка?", "Choice", True, ("Да", "Нет"), 31, 29),
    31: Question(31, "24. Возникали ли у Вас когда-либо внезапные нарушения зрения в одном или обоих глазах (видите мерцание, "
                    "полосы, пятна, пелену, туман, ухудшение зрения, двоение, четкость видения)?", "Choice", True, ("Да", "Нет"), 32, 30),
    32: Question(32, "25. Возникала ли у Вас когда-либо внезапно кратковременная потеря зрения на один глаз?", "Choice", True, ("Да", "Нет"), 33, 31),
    33: Question(33, "26. Бывают ли у Вас свистящие или жужжащие хрипы в грудной клетке при дыхании, не проходящие при откашливании?", "Choice", True, ("Да", "Нет"), 34, 32),
    34: Question(34, "27. Бывает ли у Вас кашель с мокротой?", "Choice", True, ("Да", "Нет"), 35, 33),
    35: Question(35, "28. Беспокоят ли Вас боли в области верхней части живота (в области желудка), отрыжка, тошнота, рвота, "
                    "ухудшение или отсутствие аппетита?", "Choice", True, ("Да", "Нет"), 36, 34),
    36: Question(36, "29. Бывает ли у Вас неоформленный (полужидкий) черный или дегтеобразный стул?", "Choice", True, ("Да", "Нет"), 37, 35),
    37: Question(37, "30. Бывают ли у Вас запоры?", "Choice", True, ("Да", "Нет"), 38, 36),
    38: Question(38, "31. Бывает ли у Вас боль в области заднепроходного отверстия?", "Choice", True, ("Да", "Нет"), 39, 37),
    39: Question(39, "32. Бывают ли у Вас кровяные выделения с калом?", "Choice", True, ("Да", "Нет"), 40, 38),
    # Конец symptoms

    # Начало lifestyle
    40: Question(40, "33. Курите ли Вы? (курение одной и более сигарет в день)", "Choice", True, ("Да", "Нет"), 41, 39),
    41: Question(41, "33_1. Сколько в среднем сигарет в день выкуриваете?", "String", False, None, 42, 40, 40),
    42: Question(42, "34. Сколько минут в день Вы тратите на ходьбу в умеренном или быстром темпе (включая дорогу до места "
            "работы и обратно)?", "Choice", True, ("До 30 минут", "30 минут и более"), 43, 40),
    43: Question(43, "35. Присутствует ли в Вашем ежедневном рационе 400-500 г сырых овощей и фруктов?", "Choice", True, ("Да", "Нет"), 44, 42),
    44: Question(44, "36. Имеете ли Вы привычку подсаливать приготовленную пищу, не пробуя ее?", "Choice", True, ("Да", "Нет"), 45, 43),
    45: Question(45, "37. Принимали ли Вы за последний год психотропные или наркотические вещества без назначения врача?", "Choice", True, ("Да", "Нет"), 46, 44),

    46: Question(46, "38. Как часто Вы употребляете алкогольные напитки?", "Choice", True, ("Никогда (0 баллов)", "Раз в месяц и реже (1 балл)",
            "2-4 раза в месяц (2 балла)", "2-3 раза в неделю (3 балла)", "≥ 4 раз в неделю (4 балла)"), 47, 45),
    47: Question(47, "39. Какое количество алкогольных напитков (сколько порций) вы выпиваете обычно за один раз? 1 порция равна "
            "12 мл чистого этанола ИЛИ 30 мл крепкого алкоголя (водки) ИЛИ 100 мл сухого вина ИЛИ 300 мл пива", "Choice", True, ("1-2 порции (0 баллов)",
            "3-4 порции (1 балл)", "5-6 порций (2 балла)", "7-9 порций (3 балла)", "≥ 10 порций (4 балла)"), 48, 46),
    48: Question(48, "40. Как часто Вы употребляете за один раз 6 или более порций? 6 порций равны ИЛИ 180 мл крепкого алкоголя ("
            "водки) ИЛИ 600 мл сухого вина ИЛИ 1,8 л пива", "Choice", True, ("Никогда (0 баллов)", "Раз в месяц и реже (1 балл)", "2-4 раза в месяц (2 балла)",
            "2-3 раза в неделю (3 балла)", "≥ 4 раз в неделю (4 балла)"), 49, 47),
    # Конец lifestyle

    # Начало additional_complaints
    49: Question(49, "41. Есть ли у Вас другие жалобы на свое здоровье, не вошедшие в настоящую анкету и которые Вы бы хотели "
                 "сообщить врачу (фельдшеру)", "Choice", True, ("Да", "Нет"), None, 48),
}

def get_next_question_id_by_id(answer: str, id: int):
    child_question_is_yes = [8, 15, 19, 21, 25, 27, 40]
    child_question_is_no = [1]
    if id in questions:
        question = questions[id]
        if question.next_question_id is not None:  # Add a check for None
            next_question = questions[int(question.next_question_id)]  # Convert to int
            if next_question.parent_question_id:
                if (answer == 'Да' and id in child_question_is_yes) or (answer == 'Нет' and id in child_question_is_no):
                    return question.next_question_id
                else:
                    return question.next_question_id + 1
            else:
                return question.next_question_id
    return None

def get_question_by_id(id: int) -> Question | None:
    if id in questions:
        return questions[id]
    return None
def get_last_question_by_id(id: int) -> Question | None:
    if id in questions:
        question = questions[id]
        if question.previous_question_id is None:  # Add a check for None
            return None
        last_question = get_question_by_id(question.previous_question_id)
        if last_question:
            if not last_question.parent_question_id:  # Add a check for last_question
                return last_question
            else:
                last_question = get_question_by_id(last_question.parent_question_id)
                return last_question

    return None
def get_next_question_by_id(id: int, answer: str) -> Question | None:
    next_id = get_next_question_id_by_id(answer, id)
    if next_id is None:
        return None
    return get_question_by_id(next_id)

def get_first_question() -> Question:
    return questions[0]

def get_question_type(id: int) -> QuestionType | None:
    if questions[id].question_type == QuestionType.CHOICE.value:
        return QuestionType.CHOICE
    elif questions[id].question_type == QuestionType.DATE.value:
        return QuestionType.DATE
    elif questions[id].question_type == QuestionType.TEXT.value:
        return QuestionType.TEXT