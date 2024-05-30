## ИСПОЛЬЗОВАНИЕ
1. Установить MySQL
2. Создать и войти в базу данных с помощью команды:
``` MySQl
CREATE DATABASE medical_survey_database;
USE medical_survey_database;
```
3. Создать Таблицы с помощью команды:
``` MySQL
CREATE TABLE medical_survey (
    policy_number VARCHAR(16) PRIMARY KEY,
    survey_date DATE,
    patient_name VARCHAR(255),
    gender VARCHAR(10),
    birth_date DATE,
    age INT,
    medical_organization VARCHAR(255),
    doctor_name VARCHAR(255),
    additional_complaints BOOLEAN
);

CREATE TABLE conditions (
    policy_number VARCHAR(16),
    condition_name VARCHAR(255),
    diagnosed BOOLEAN,
    medication BOOLEAN,
    type VARCHAR(64),
    PRIMARY KEY (policy_number, condition_name),
    FOREIGN KEY (policy_number) REFERENCES medical_survey(policy_number) ON DELETE CASCADE
);

CREATE TABLE health_events (
    policy_number VARCHAR(16),
    event_name VARCHAR(255),
    occurred BOOLEAN,
    PRIMARY KEY (policy_number, event_name),
    FOREIGN KEY (policy_number) REFERENCES medical_survey(policy_number) ON DELETE CASCADE
);

CREATE TABLE family_history (
    policy_number VARCHAR(16),
    condition_name VARCHAR(255),
    diagnosed BOOLEAN,
    condition_type VARCHAR(255),
    PRIMARY KEY (policy_number, condition_name),
    FOREIGN KEY (policy_number) REFERENCES medical_survey(policy_number) ON DELETE CASCADE
);

CREATE TABLE symptoms (
    policy_number VARCHAR(16),
    symptom_name VARCHAR(255),
    present BOOLEAN,
    PRIMARY KEY (policy_number, symptom_name),
    FOREIGN KEY (policy_number) REFERENCES medical_survey(policy_number) ON DELETE CASCADE
);

CREATE TABLE lifestyle (
    policy_number VARCHAR(16),
    habit_name VARCHAR(255),
    value VARCHAR(255),
    PRIMARY KEY (policy_number, habit_name),
    FOREIGN KEY (policy_number) REFERENCES medical_survey(policy_number) ON DELETE CASCADE
);
```
4. Получить имя Хоста через команду:
``` MySQL
SHOW VARIABLES LIKE 'hostname';
```
5. Записать hostname данные в config.py
6. Записать все необходимые поля в config.py
7. Установить зависимости pip -r requirements.txt
8. Запустить bot.py
### DEPENDENCIES
 - Python 3.12
### TODO:
- [x] Реализовать finite state machine (реализовать состояния)  
