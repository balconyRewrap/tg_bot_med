from Questions import questions, Question, QuestionType
from datetime import datetime
from MedicalSurvey import MedicalSurvey


fields_dict = {
    0: 'policy_number',
    1: 'nothing',
    2: 'survey_date',
    3: 'patient_name',
    4: 'gender',
    5: 'birth_date',
    6: 'medical_organization',
    7: 'doctor_name',

    8: 'hypertension',
    9: 'hypertension',
    10: 'ischemic_heart_disease',
    11: 'cerebrovascular_disease',
    12: 'chronic_lung_disease',
    13: 'tuberculosis',
    14: 'diabetes',
    15: 'diabetes',
    16: 'stomach_disease',
    17: 'chronic_kidney_disease',
    18: 'cancer',
    19: 'cancer',
    20: 'high_cholesterol',
    21: 'high_cholesterol',

    22: 'myocardial_infarction',
    23: 'stroke',

    24: 'heart_attack_or_stroke',
    25: 'cancer',
    26: 'cancer',

    27: 'chest_pain',
    28: 'chest_pain_disappears',
    29: 'sudden_weakness',
    30: 'sudden_numbness',
    31: 'sudden_vision_loss',
    32: 'sudden_one_eye_vision_loss',
    33: 'wheezing',
    34: 'coughing_blood',
    35: 'upper_abdominal_pain',
    36: 'black_stool',
    37: 'unexplained_weight_loss',
    38: 'anal_pain',
    39: 'blood_in_stool',

    40: 'smoking',
    41: 'cigarettes_per_day',
    42: 'walking_minutes_per_day',
    43: 'vegetable_fruit_intake',
    44: 'salt_habit',
    45: 'drug_use',
    46: 'alcohol_frequency',
    47: 'alcohol_portions',
    48: 'binge_drinking_frequency',

    49: 'additional_complaints'

}

def handle_answer(question_id: int, survey: MedicalSurvey, message):
    if question_id in range(0, 8):
        handle_q0_to_q7(questions[question_id], survey, message)
    elif question_id in range(8, 22):
        handle_q8_to_q21(questions[question_id], survey, message)
    elif question_id in range(22, 24):
        handle_q22_to_q23(questions[question_id], survey, message)
    elif question_id in range(24, 27):
        handle_q24_to_q26(questions[question_id], survey, message)
    elif question_id in range(27, 40):
        handle_q27_to_q39(questions[question_id], survey, message)
    elif question_id in range(40, 46):
        handle_q40_to_q45(questions[question_id], survey, message)
    elif question_id in range(46, 49):
        handle_q46_to_q48(questions[question_id], survey, message)
    elif question_id == 49:
        handle_q49(questions[question_id], survey, message)

def save_survey_date(survey):
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d-%m-%Y")
    survey.survey_date = formatted_date

def handle_q0_to_q7(question: Question, survey : MedicalSurvey, message):
    if question.question_type == QuestionType.TEXT.value:
        setattr(survey, fields_dict[question.id], message.text)
    elif question.question_type == QuestionType.DATE.value:
        date = datetime.strptime(message.text, "%d-%m-%Y")
        setattr(survey, fields_dict[question.id], date.strftime("%d-%m-%Y"))
        if survey.survey_date is not None:
            survey_date = datetime.strptime(survey.survey_date, "%d-%m-%Y")

            age = survey_date.year - date.year
            if (date.month, survey_date.day) < (date.month, survey_date.day):
                age -= 1
            survey.age = age
    elif question.question_type == QuestionType.CHOICE.value:
        if not(message.text in question.options):
            raise ValueError("Invalid option")
        if question.id == 1:  # first question doesnt need to be handled
            return


        setattr(survey, fields_dict[question.id], message.text)

def handle_q8_to_q21(question: Question, survey : MedicalSurvey, message):
    if question.question_type == QuestionType.TEXT.value:
        survey.set_condition(fields_dict[question.id], diagnosed = True, type = message.text)
    elif question.question_type == QuestionType.CHOICE.value:
        if not(message.text in question.options):
            raise ValueError("Invalid option")
        if message.text == "Да":
            survey.set_condition(fields_dict[question.id], diagnosed = True)
        elif message.text == "Да" and question.id == 9:
            survey.set_condition(fields_dict[question.id], diagnosed = True, medication = True)
        else:
            survey.set_condition(fields_dict[question.id], diagnosed = False)

def handle_q22_to_q23(question: Question, survey : MedicalSurvey, message):
    if not(message.text in question.options):
            raise ValueError("Invalid option")
    if message.text == "Да":
        survey.set_health_event(fields_dict[question.id], occurred = True)
    else:
        survey.set_health_event(fields_dict[question.id], occurred = True)
    

def handle_q24_to_q26(question: Question, survey : MedicalSurvey, message):
    if question.question_type == QuestionType.TEXT.value:
        survey.set_family_history(fields_dict[question.id], diagnosed = True, type = message.text)
    elif question.question_type == QuestionType.CHOICE.value:
        if not(message.text in question.options):
            raise ValueError("Invalid option")
        if message.text == "Да":
            survey.set_family_history(fields_dict[question.id], diagnosed = True)
        else:
            survey.set_family_history(fields_dict[question.id], diagnosed = False)

def handle_q27_to_q39(question: Question, survey : MedicalSurvey, message): 
    if not(message.text in question.options):
            raise ValueError("Invalid option")
    if message.text == "Да":
        survey.set_symptom(fields_dict[question.id], True)
    else:
        survey.set_symptom(fields_dict[question.id], False)

def handle_q40_to_q45(question: Question, survey : MedicalSurvey, message):
    if question.question_type == QuestionType.TEXT.value:
        additional_info = int(message.text)
        survey.set_lifestyle(fields_dict[question.id], additional_info)
    elif question.question_type == QuestionType.CHOICE.value:
        if not(message.text in question.options):
            raise ValueError("Invalid option")
        if message.text == "Да" or message.text == "30 минут и более":
            survey.set_lifestyle(fields_dict[question.id], value = True)
        elif message.text == "Нет" or message.text == "До 30 минут":
            survey.set_lifestyle(fields_dict[question.id], value = False)



def handle_q46_to_q48(question: Question, survey : MedicalSurvey, message):
    score_0 = ["Никогда (0 баллов)", "1-2 порции (0 баллов)", "Никогда (0 баллов)"]
    score_1 = ["Раз в месяц и реже (1 балл)",  "3-4 порции (1 балл)"]
    score_2 = ["2-4 раза в месяц (2 балла)", "5-6 порций (2 балла)"]
    score_3 = ["2-3 раза в неделю (3 балла)", "7-9 порций (3 балла)"]
    score_4 = ["≥ 4 раз в неделю (4 балла)", "≥ 10 порций (4 балла)"]
    if not(message.text in question.options):
        raise ValueError("Invalid option")
    if message.text in score_0:
        survey.set_lifestyle(fields_dict[question.id], 0)
    elif message.text in score_1:
        survey.set_lifestyle(fields_dict[question.id], 1)
    elif message.text in score_2:
        survey.set_lifestyle(fields_dict[question.id], 2)
    elif message.text in score_3:
        survey.set_lifestyle(fields_dict[question.id], 3)
    elif message.text in score_4:
        survey.set_lifestyle(fields_dict[question.id], 4)

def handle_q49(question: Question, survey : MedicalSurvey, message):
    if not(message.text in question.options):
        raise ValueError("Invalid option")
    if message.text == "Да":
        survey.set_additional_complaints(complaints=True)
    elif message.text == "Нет":
        survey.set_additional_complaints(complaints=False)

