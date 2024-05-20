import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD
from MedicalSurvey import MedicalSurvey
from datetime import datetime
# Устанавливаем соединение с базой данных


# Создаем объект курсора для выполнения SQL-запросов



def add_medical_survey(medical_survey):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database="medical_survey_database"
    )
    cursor = conn.cursor()
    try:
        survey_date = datetime.strptime(medical_survey.survey_date, '%d-%m-%Y').date()
        birth_date = datetime.strptime(medical_survey.birth_date, '%d-%m-%Y').date()
        # Добавляем основную информацию об опросе в таблицу medical_survey
        sql = "REPLACE INTO medical_survey (policy_number, survey_date, patient_name, gender, birth_date, age, medical_organization, doctor_name, additional_complaints) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            medical_survey.policy_number, survey_date, medical_survey.patient_name,
            medical_survey.gender,
            birth_date, medical_survey.age, medical_survey.medical_organization,
            medical_survey.doctor_name,
            int(medical_survey.additional_complaints)))
        print(1)
        # Добавляем данные о состояниях в таблицу conditions
        for condition, data in medical_survey.conditions.items():
            if condition == 'hypertension' or condition == 'diabetes' or condition == 'high_cholesterol':
                sql = "REPLACE INTO conditions (policy_number, condition_name, diagnosed, medication) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (medical_survey.policy_number, condition, int(data['diagnosed']), int(data['medication'])))
            elif condition == 'cancer':
                sql = "REPLACE INTO conditions (policy_number, condition_name, diagnosed, type) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (medical_survey.policy_number, condition, int(data['diagnosed']), data['type']))
            else:
                sql = "REPLACE INTO conditions (policy_number, condition_name, diagnosed) VALUES (%s, %s, %s)"
                cursor.execute(sql, (medical_survey.policy_number, condition, int(data)))

        print(2)
        # Добавляем данные о событиях здоровья в таблицу health_events
        for event, occurred in medical_survey.health_events.items():
            sql = "REPLACE INTO health_events (policy_number, event_name, occurred) VALUES (%s, %s, %s)"
            cursor.execute(sql, (medical_survey.policy_number, event, int(occurred)))
        print(3)
        # Добавляем данные о семейном анамнезе в таблицу family_history
        for condition, data in medical_survey.family_history.items():
            if condition == 'cancer':
                sql = "REPLACE INTO family_history (policy_number, condition_name, diagnosed, condition_type) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (medical_survey.policy_number, condition, int(data['diagnosed']), data['type']))
            else:
                sql = "REPLACE INTO family_history (policy_number, condition_name, diagnosed) VALUES (%s, %s, %s)"
                cursor.execute(sql, (medical_survey.policy_number, condition, int(data)))
        print(4)
        # Добавляем данные о симптомах в таблицу symptoms
        for symptom, present in medical_survey.symptoms.items():
            sql = "REPLACE INTO symptoms (policy_number, symptom_name, present) VALUES (%s, %s, %s)"
            cursor.execute(sql, (medical_survey.policy_number, symptom, int(present)))
        print(5)
        # Добавляем данные об образе жизни в таблицу lifestyle
        for habit, value in medical_survey.lifestyle.items():
            sql = "REPLACE INTO lifestyle (policy_number, habit_name, value) VALUES (%s, %s, %s)"
            cursor.execute(sql, (medical_survey.policy_number, habit, int(value)))
        print(6)
        # Подтверждаем изменения в базе данных
        conn.commit()
        print("Объект MedicalSurvey успешно добавлен в базу данных!")
    except mysql.connector.Error as error:
        print("Ошибка при добавлении объекта MedicalSurvey в базу данных:", error)
    finally:
        # Закрываем курсор и соединение
        cursor.close()
        conn.close()


def get_medical_survey(policy_number):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database="medical_survey_database"
    )
    cursor = conn.cursor()
    try:
        # Получаем основную информацию об опросе из таблицы medical_survey
        sql = "SELECT * FROM medical_survey WHERE policy_number = %s"
        cursor.execute(sql, (policy_number,))
        medical_survey_data = cursor.fetchone()

        if medical_survey_data:
            # Создаем объект MedicalSurvey и заполняем его данными
            survey = MedicalSurvey(policy_number)
            survey.survey_date = medical_survey_data[1]
            survey.patient_name = medical_survey_data[2]
            survey.gender = medical_survey_data[3]
            survey.birth_date = medical_survey_data[4]
            survey.age = medical_survey_data[5]
            survey.medical_organization = medical_survey_data[6]
            survey.doctor_name = medical_survey_data[7]
            survey.additional_complaints = bool(medical_survey_data[8])

            # Получаем данные об условиях из таблицы conditions
            sql = "SELECT condition_name, diagnosed, medication, type FROM conditions WHERE policy_number = %s"
            cursor.execute(sql, (policy_number,))
            conditions_data = cursor.fetchall()

            for condition in conditions_data:
                if condition[0] == 'hypertension' or condition[0] == 'diabetes' or condition[0] == 'high_cholesterol':
                    survey.set_condition(condition[0], bool(condition[1]), bool(condition[2]))
                elif condition == 'cancer':
                    survey.set_condition(condition[0], bool(condition[1]), str(condition[2]))
                else:
                    survey.set_condition(condition[0], bool(condition[1]))

            # Получаем данные о событиях здоровья из таблицы health_events
            sql = "SELECT event_name, occurred FROM health_events WHERE policy_number = %s"
            cursor.execute(sql, (policy_number,))
            health_events_data = cursor.fetchall()
            for health_event in health_events_data:
                survey.set_health_event(health_event[0], bool(health_event[1]))

            # Получаем данные о семейном анамнезе из таблицы family_history
            sql = "SELECT condition_name, diagnosed, condition_type FROM family_history WHERE policy_number = %s"
            cursor.execute(sql, (policy_number,))
            family_history_data = cursor.fetchall()
            for condition in family_history_data:
                if condition[0] == 'cancer':
                    survey.set_family_history(condition[0], bool(condition[1]), str(condition[2]))
                else:
                    survey.set_family_history(condition[0], bool(condition[1]))


            # Получаем данные о симптомах из таблицы symptoms
            sql = "SELECT symptom_name, present FROM symptoms WHERE policy_number = %s"
            cursor.execute(sql, (policy_number,))
            symptoms_data = cursor.fetchall()
            for symptom_data in symptoms_data:
                survey.set_symptom(symptom_data[0], bool(symptom_data[1]))

            # Получаем данные об образе жизни из таблицы lifestyle
            sql = "SELECT habit_name, value FROM lifestyle WHERE policy_number = %s"
            cursor.execute(sql, (policy_number,))
            lifestyles_data = cursor.fetchall()
            for lifestyle_data in lifestyles_data:
                if (lifestyle_data[0] == 'smoking' or lifestyle_data[0] == 'vegetable_fruit_intake' or
                        lifestyle_data[0] == 'salt_habit' or lifestyle_data[0] == 'drug_use'):
                    survey.set_lifestyle(lifestyle_data[0], bool(lifestyle_data[1]))
                else:
                    survey.set_lifestyle(lifestyle_data[0], int(lifestyle_data[1]))

            return survey
        else:
            print("Объект MedicalSurvey с указанным номером полиса не найден в базе данных")
            return None
    except mysql.connector.Error as error:
        print("Ошибка при получении объекта MedicalSurvey из базы данных:", error)
    finally:
        # Закрываем курсор и соединение
        cursor.close()
        conn.close()


# Пример использования
if __name__ == "__main__":
    survey1 = MedicalSurvey("123412341234", "01-01-2024", "Уву Имя Отчество", "Муж", "01-01-2005", "19", "Медицинская Организация", "ФИО Позиция")
    survey1.set_condition('hypertension', True, True)
    survey1.set_condition('ischemic_heart_disease', True)
    survey1.set_condition('cerebrovascular_disease', False)
    survey1.set_condition('chronic_lung_disease', False)
    survey1.set_condition('tuberculosis', True)
    survey1.set_condition('diabetes', diagnosed=True, medication=False)
    survey1.set_condition('stomach_disease', False)
    survey1.set_condition('chronic_kidney_disease', True)
    survey1.set_condition('canser', True, "Рак Жопы")
    survey1.set_health_event('myocardial_infarction', True)
    survey1.set_family_history('cancer', True, "Рак простаты")
    survey1.set_symptom('chest_pain', True)
    survey1.set_symptom('wheezing', True)
    survey1.set_lifestyle('smoking', True)
    survey1.set_lifestyle('cigarettes_per_day', 10)
    survey1.set_lifestyle('alcohol_frequency', 4)
    survey1.set_lifestyle('score', 4)
    survey1.set_additional_complaints(True)
    # Создание объекта MedicalSurvey
    add_medical_survey(survey1)  # Добавление объекта в базу данных
    survey2 = get_medical_survey("123412341234")
    survey2.print_fields()