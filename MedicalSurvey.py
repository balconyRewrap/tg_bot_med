from typing import Optional, Union, Tuple 
class MedicalSurvey:
    def __init__(self, policy_number: str, survey_date: Optional[str] = None, patient_name: Optional[str] = None,
                 gender: Optional[str] = None, birth_date: Optional[str] = None, age: Optional[int] = None,
                 medical_organization: Optional[str] = None, doctor_name: Optional[str] = None) -> None:
        self.policy_number = policy_number
        self.survey_date = survey_date
        self.patient_name = patient_name
        self.gender = gender
        self.birth_date = birth_date
        self.age = age
        self.medical_organization = medical_organization
        self.doctor_name = doctor_name

        self.conditions = {
            'hypertension': {'diagnosed': False, 'medication': False},
            'ischemic_heart_disease': False,
            'cerebrovascular_disease': False,
            'chronic_lung_disease': False,
            'tuberculosis': False,
            'diabetes': {'diagnosed': False, 'medication': False},
            'stomach_disease': False,
            'chronic_kidney_disease': False,
            'cancer': {'diagnosed': False, 'type': ''},
            'high_cholesterol': {'diagnosed': False, 'medication': False}
        }

        self.health_events: dict[str, bool] = {
            'myocardial_infarction': False,
            'stroke': False
        }

        self.family_history: dict[str, Union[bool, dict[str, Union[bool, str]]]] = {
            'heart_attack_or_stroke': False,
            'cancer': {'diagnosed': False, 'type': ''},
        }

        self.symptoms: dict[str, bool] = {
            'chest_pain': False,
            'chest_pain_disappears': False,
            'sudden_weakness': False,
            'sudden_numbness': False,
            'sudden_vision_loss': False,
            'chronic_cough': False,
            'wheezing': False,
            'coughing_blood': False,
            'upper_abdominal_pain': False,
            'black_stool': False,
            'unexplained_weight_loss': False,
            'anal_pain': False,
            'blood_in_stool': False
        }

        self.lifestyle: dict[str, Union[bool, int]] = {
            'smoking': False,
            'cigarettes_per_day': 0,
            'walking_minutes_per_day': 0,
            'vegetable_fruit_intake': False,
            'salt_habit': False,
            'drug_use': False,
            'alcohol_frequency': 0,
            'alcohol_portions': 0,
            'binge_drinking_frequency': 0,
            'score': 0
        }

        self.additional_complaints: bool = False

        self.translations: dict[str, str] = {
            'hypertension': 'Гипертония',
            'ischemic_heart_disease': 'Ишемическая болезнь сердца',
            'cerebrovascular_disease': 'Сосудистые заболевания головного мозга',
            'chronic_lung_disease': 'Хронические заболевания легких',
            'tuberculosis': 'Туберкулез',
            'diabetes': 'Диабет',
            'stomach_disease': 'Заболевания желудка',
            'chronic_kidney_disease': 'Хронические заболевания почек',
            'cancer': 'Рак',
            'high_cholesterol': 'Высокий холестерин',
            'myocardial_infarction': 'Инфаркт миокарда',
            'stroke': 'Инсульт',
            'heart_attack_or_stroke': 'Инфаркт или инсульт',
            'chest_pain': 'Боль в груди',
            'chest_pain_disappears': 'Боль в груди исчезает в течение 20 минут или после приема нитроглицерина',
            'sudden_weakness': 'Внезапная слабость',
            'sudden_numbness': 'Внезапное онемение',
            'sudden_vision_loss': 'Внезапная потеря зрения',
            'chronic_cough': 'Хронический кашель',
            'wheezing': 'Свист в груди',
            'coughing_blood': 'Кашель с кровью',
            'upper_abdominal_pain': 'Боль в верхней части живота',
            'black_stool': 'Неоформленный (полужидкий) черный или дегтеобразный стул',
            'unexplained_weight_loss': 'Необъяснимая потеря веса за последнее время',
            'anal_pain': 'Боль в области ануса',
            'blood_in_stool': 'Кровяные выделения с калом',
            'smoking': 'Курение',
            'cigarettes_per_day': 'Количество сигарет в день',
            'walking_minutes_per_day': 'Продолжительность ходьбы в минутах в день',
            'vegetable_fruit_intake': 'Употребление овощей и фруктов',
            'salt_habit': 'Привычка к соли',
            'drug_use': 'Употребление наркотиков',
            'alcohol_frequency': 'Частота употребления алкоголя',
            'alcohol_portions': 'Количество порций алкоголя',
            'binge_drinking_frequency': 'Частота пьянства',
            'score': 'Оценка'
        }

    def set_condition(self, condition: str, diagnosed: bool, medication: bool = False, type: str = '') -> None:
        if condition in self.conditions:
            if isinstance(self.conditions[condition], dict):
                if condition == 'cancer':
                    self.conditions[condition]['diagnosed'] = diagnosed
                    if type != '':
                        self.conditions[condition]['type'] = type
                else:
                    self.conditions[condition]['diagnosed'] = diagnosed
                    if medication is not None:
                        self.conditions[condition]['medication'] = medication
            else:
                self.conditions[condition] = diagnosed

    def set_health_event(self, event: str, occurred: bool) -> None:
        if event in self.health_events:
            self.health_events[event] = occurred

    def set_family_history(self, condition: str, present: bool, details: Optional[str] = None) -> None:
        if condition in self.family_history:

            if condition == 'cancer':
                if details != None:
                    self.family_history['cancer'] = {'diagnosed': present, 'type': details}
            else:
                self.family_history[condition] = present

    def set_symptom(self, symptom: str, present: bool) -> None:
        if symptom in self.symptoms:
            self.symptoms[symptom] = present

    def set_lifestyle(self, habit: str, value: Union[bool, int]) -> None:
        if habit in self.lifestyle:
            if habit in ['alcohol_frequency', 'alcohol_portions', 'binge_drinking_frequency']:
                if value not in range(0, 5):
                    raise ValueError(f"{habit} must be between 0 and 4")
            self.lifestyle[habit] = value

    def calculate_score(self) -> None:
        self.lifestyle['score'] = self.lifestyle['alcohol_frequency'] + self.lifestyle['alcohol_portions'] + \
                                  self.lifestyle['binge_drinking_frequency']

    def set_additional_complaints(self, complaints: bool) -> None:
        self.additional_complaints = complaints

    def format_data_as_html(self) -> Tuple[str, str, str, str, str, str, str]:
        formatted_data_main: str = "<b>Информация об анкете пациенте с номером полиса:</b>" + f"{self.policy_number}\n\n"
        formatted_data_main += f"<b>Дата Прохождения Диспансеризации:</b> {self.survey_date}\n"
        formatted_data_main += f"<b>Ф.И.О. Пациента:</b> {self.patient_name}\n"
        formatted_data_main += f"<b>Пол:</b> {self.gender}\n"
        formatted_data_main += f"<b>Дата Рождения:</b> {self.birth_date}\n"
        formatted_data_main += f"<b>Полных Лет:</b> {self.age}\n"
        formatted_data_main += f"<b>Медицинская Организация:</b> {self.medical_organization}\n"
        formatted_data_main += (f"<b>Должность и Ф.И.О. медицинского работника, проводящего анкетирование и подготовку "
                                f"заключения по его результатам: :</b> {self.doctor_name}\n")

        formatted_data_conditions: str = "<b>Говорил ли когда-либо пациенту врач, что у него имеется:</b>\n"
        for condition, data in self.conditions.items():
            if condition == 'hypertension' or condition == 'diabetes' or condition == 'high_cholesterol':

                formatted_data_conditions += f"<b>{self.translations[condition]}</b>: "

                if data['diagnosed']:
                    formatted_data_conditions += "Диагностировано"
                    formatted_data_conditions += ", "

                    if data['medication']:
                        formatted_data_conditions += "Лекарство принимается"
                    else:
                        formatted_data_conditions += "Лекарство не принимается"
                else:
                    formatted_data_conditions += "Не диагностировано"

                formatted_data_conditions += "\n"

            elif condition == 'cancer':
                formatted_data_conditions += f"<b>{self.translations[condition]}</b>: "
                if data['diagnosed']:
                    formatted_data_conditions += f"Диагностировано, Тип - {data['type']} \n"
                else:
                    formatted_data_conditions += "Не диагностировано" + "\n"
            else:
                formatted_data_conditions += (f"<b>{self.translations[condition]}</b>: " +
                                              f"{'Диагностировано' if data else 'Не диагностировано'}\n")
        formatted_data_health_events: str = ""
        formatted_data_health_events += "<b>Произошли ли у пациента следующие события:</b>\n"
        for event, occurred in self.health_events.items():
            formatted_data_health_events += (f"<b>{self.translations[event]}</b>: "
                                             + f"{'Произошло' if occurred else 'Не произошло'}\n")
        formatted_data_family_history: str = ""
        formatted_data_family_history += "Были ли у близких родственников пациента следующие события:\n"
        for condition, present in self.family_history.items():
            if condition == 'cancer' and isinstance(present, dict):
                formatted_data_family_history += f"<b>{self.translations[condition]}</b>: "
                if present['diagnosed']:
                    formatted_data_family_history += f"Было. Тип - {present['type']}\n"
                else:
                    formatted_data_family_history += 'Не было\n'
            else:
                formatted_data_family_history += (f"<b>{self.translations[condition]}</b>: " +
                                                  f"{f'Было.' if present else 'Не было'}\n")
        formatted_data_symptoms: str = ""
        formatted_data_symptoms += "Возникало ли у пациента следующее:\n"
        for symptom, present in self.symptoms.items():
            if symptom == 'chest_pain':
                if present:
                    formatted_data_symptoms += f"<b>{self.translations[symptom]}</b>: Возникало.\n"
                    if self.symptoms['chest_pain_disappears']:
                        formatted_data_symptoms += (f"У пациента исчезает боль сразу или в течение не более чем 20 "
                                                    f"мин после"
                                                    f"прекращения ходьбы/адаптации к холоду/ в тепле/в покое и (или) "
                                                    f"они исчезают через 1-5 мин после приема нитроглицерина\n")
                    else:
                        formatted_data_symptoms += (f"У пациента не исчезает боль сразу или в течение не более чем 20 "
                                                    f"мин после"
                                                    f"прекращения ходьбы/адаптации к холоду/ в тепле/в покое и (или) "
                                                    f"они исчезают через 1-5 мин после приема нитроглицерина\n")
            elif symptom == 'chest_pain_disappears':
                continue
            else:
                formatted_data_symptoms += (f"<b>{self.translations[symptom]}</b>: " +
                                            f"{f'Возникало.' if present else 'Не возникало'}\n")

        formatted_data_lifestyle: str = ""
        formatted_data_lifestyle += "Стиль жизни пациента:\n"
        for habit, value in self.lifestyle.items():
            if habit == 'cigarettes_per_day':
                continue
            elif habit == 'smoking':
                if value:
                    formatted_data_lifestyle += ("<b>Пациент курит</b>" + f" и выкуривает "
                                                                          f"{self.lifestyle['cigarettes_per_day']} "
                                                                          f"сигарет в день\n")
                else:
                    formatted_data_lifestyle += "<b>Пациент не курит</b>"
            elif habit == 'walking_minutes_per_day':
                formatted_data_lifestyle += ("<b>Пациент гуляет:</b> " +
                                             f"{'Более 30 минут в день' if value == 30 else 'Менее 30 минут в день'}\n")
            elif habit == 'vegetable_fruit_intake':
                if value:
                    formatted_data_lifestyle += ("<b>В ежедневном рационе пациента присутствует 400-500 г сырых овощей "
                                                 "и фруктов</b>\n")
                else:
                    formatted_data_lifestyle += ("<b>В ежедневном рационе пациента присутствует менее 400-500 г сырых "
                                                 "овощей и фруктов</b>\n")
            elif habit == 'salt_habit':
                if value:
                    formatted_data_lifestyle += ("<b>Пациент имеет привычку подсаливать приготовленную пищу, не пробуя "
                                                 "ее</b>\n")
                else:
                    formatted_data_lifestyle += ("<b>Пациент не имеет привычку подсаливать приготовленную пищу, "
                                                 "не пробуя ее</b>\n")
            elif habit == 'drug_use':
                if value:
                    formatted_data_lifestyle += ("<b>Пациент принимал за последний год психотропные или наркотические "
                                                 "вещества без назначения врача</b>\n")
                else:
                    formatted_data_lifestyle += ("<b>Пациент не принимал за последний год психотропные или "
                                                 "наркотические вещества без назначения врача</b>\n")
            elif habit == 'alcohol_frequency':
                formatted_data_lifestyle += "<b>Пациент принимает алкоголь со следующей частотой</b>: "
                if value == 0:
                    formatted_data_lifestyle += "Никогда (0 баллов) \n"
                elif value == 1:
                    formatted_data_lifestyle += "Раз в месяц и реже (1 балл) \n"
                elif value == 2:
                    formatted_data_lifestyle += "2-4 раза в месяц (2 балла)  \n"
                elif value == 3:
                    formatted_data_lifestyle += "2-3 раза в неделю (3 балла)  \n"
                elif value == 4:
                    formatted_data_lifestyle += "≥ 4 раз в неделю (4 балла)  \n"
            elif habit == 'alcohol_portions':
                formatted_data_lifestyle += ("<b>Пациент выписывает обычно за раз следующее количество алкогольных "
                                             "напитков (сколько порций)</b>:")
                if value == 0:
                    formatted_data_lifestyle += "1-2 порции (0 баллов) \n"
                elif value == 1:
                    formatted_data_lifestyle += "3-4 порции (1 балл) \n"
                elif value == 2:
                    formatted_data_lifestyle += "5-6 порции (2 балла)  \n"
                elif value == 3:
                    formatted_data_lifestyle += "7-9 порции  \n"
                elif value == 4:
                    formatted_data_lifestyle += "≥ 10 порции  \n"
            elif habit == 'binge_drinking_frequency':
                formatted_data_lifestyle += "<b>Пациент принимает 6 или более порций со следующей частотой</b>: "
                if value == 0:
                    formatted_data_lifestyle += "Никогда (0 баллов) \n"
                elif value == 1:
                    formatted_data_lifestyle += "Раз в месяц и реже (1 балл) \n"
                elif value == 2:
                    formatted_data_lifestyle += "2-4 раза в месяц (2 балла)  \n"
                elif value == 3:
                    formatted_data_lifestyle += "2-3 раза в неделю (3 балла)  \n"
                elif value == 4:
                    formatted_data_lifestyle += "≥ 4 раз в неделю (4 балла)  \n"
            elif habit == 'score':
                formatted_data_lifestyle += f"<b>Итоговая сумма баллов равна</b> {value}"

        if self.additional_complaints:
            formatted_data_additional_complaints = ("<b>У пациента есть другие жалобы на свое здоровье, не вошедшие в "
                                                    "настоящую анкету и которые он бы хотел сообщить врачу ("
                                                    "фельдшеру)</b>\n")
        else:
            formatted_data_additional_complaints = ("<b>У пациента нет других жалобы на свое здоровье, не вошедшие в "
                                                    "настоящую анкету и которые он бы хотел сообщить врачу ("
                                                    "фельдшеру)</b>\n")
        return (formatted_data_main, formatted_data_conditions, formatted_data_health_events,
                formatted_data_family_history, formatted_data_symptoms,
                formatted_data_lifestyle, formatted_data_additional_complaints)

    def print_fields(self):
        print("Medical Survey")
        print("policy number:", self.policy_number)
        print("Survey Date:", self.survey_date)
        print("Patient Name:", self.patient_name)
        print("Gender:", self.gender)
        print("Birth Date:", self.birth_date)
        print("Age:", self.age)
        print("Medical Organization:", self.medical_organization)
        print("Doctor Name:", self.doctor_name)
        print("Conditions:")
        for condition, data in self.conditions.items():
            if condition == 'hypertension' or condition == 'diabetes' or condition == 'high_cholesterol':
                print(f"  {condition}: Diagnosed - {data['diagnosed']}, Medication - {data['medication']}")
            elif condition == 'cancer':
                print(f"  {condition}: Diagnosed - {data['diagnosed']}, Type - {data['type']}")
            else:
                print(f"  {condition}: {data}")
        print("Health Events:")
        for event, occurred in self.health_events.items():
            print(f"  {event}: {occurred}")
        print("Family History:")
        for condition, present in self.family_history.items():
            if isinstance(present, list):
                print(f"  {condition}: Present - {present}")
            else:
                print(f"  {condition}: {present}")
        print("Symptoms:")
        for symptom, present in self.symptoms.items():
            print(f"  {symptom}: {present}")
        print("Lifestyle:")
        for habit, value in self.lifestyle.items():
            print(f"  {habit}: {value}")
        print("Additional Complaints:", self.additional_complaints)
