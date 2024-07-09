## USAGE
1. Install MySQL
2. Create and access the database using the command:
```MySQL
CREATE DATABASE medical_survey_database;
USE medical_survey_database;
```
3. Create the tables using the command:
```MySQL
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
4. Get the hostname using the command:
```MySQL
SHOW VARIABLES LIKE 'hostname';
```
5. Enter the hostname data into config.py
6. Fill in all necessary fields in config.py
7. Install dependencies with pip -r requirements.txt
8. Run bot.py
### DEPENDENCIES
 - Python 3.12
### TODO:
- [x] Implement finite state machine (implement states)
