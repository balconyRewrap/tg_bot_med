class MedicalSurvey:
    def __init__(self, policy_number, survey_date=None, patient_name=None, gender=None, birth_date=None, age=None,
                 medical_organization=None, doctor_name=None):
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

        self.health_events = {
            'myocardial_infarction': False,
            'stroke': False
        }

        self.family_history = {
            'heart_attack_or_stroke': False,
            'cancer': {'diagnosed': False, 'type': ''},
        }

        self.symptoms = {
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

        self.lifestyle = {
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

        self.additional_complaints = False

    def set_condition(self, condition, diagnosed, medication=None):
        if condition in self.conditions:
            if isinstance(self.conditions[condition], dict):
                self.conditions[condition]['diagnosed'] = diagnosed
                if medication is not None:
                    self.conditions[condition]['medication'] = medication
            else:
                self.conditions[condition] = diagnosed

    def set_health_event(self, event, occurred):
        if event in self.health_events:
            self.health_events[event] = occurred

    def set_family_history(self, condition, present, details=None):
        if condition in self.family_history:
            if isinstance(self.family_history[condition], list) and present:
                self.family_history[condition] = details

    def set_symptom(self, symptom, present):
        if symptom in self.symptoms:
            self.symptoms[symptom] = present

    def set_lifestyle(self, habit, value):
        if habit in self.lifestyle:
            if habit in ['alcohol_frequency', 'alcohol_portions', 'binge_drinking_frequency']:
                if value not in range(0, 5):
                    raise ValueError(f"{habit} must be between 0 and 4")
            self.lifestyle[habit] = value

    def calculate_score(self):
        self.lifestyle['score'] = self.lifestyle['alcohol_frequency'] + self.lifestyle['alcohol_portions'] + \
                                  self.lifestyle['binge_drinking_frequency']

    def set_additional_complaints(self, complaints):
        self.additional_complaints = complaints

    def print_fields(self):
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
