print("Medical Diagnose Bot")
welcome_prompt = "Welcome Doctor! Please choose an option from the menu below\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
name_prompt = "What is the patient's name?\n"
appearance_prompt = "How's the patient general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eyes_prompt = "Checking Eyes Results:\n - 1 Eyes Normal, Slightly Sunken\n - 2 Eyes Very Sunken\n"
skin_prompt = "Skin Pinch Test Results:\n - 1 Skin is Normal\n - 2 Skin is Slow\n"
normal_appearance = "Check the Eye Appearance\n"
irritable_appearance = "Do a skin pinch\n"
no_dehydration = "No Dehydration"
some_dehydration = "Some Dehydration"
severe_dehydration = "Severe Dehydration"
error_message = "Please enter a valid input"

patients_and_diagnoses = [
    "Alexander: No Dehydration",
    "Miriam: Some Dehydration",
    "Wishymashy: Severe Dehydration"
]


def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)

def save_new_diagnosis(name, diagnosis):
    if name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = name + ": " + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final Diagnosis: " + final_diagnosis + "\n")
    
def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration
    else:
        return ""

def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    elif skin == "2":
        return severe_dehydration
    else:
        return ""

def run_diagnosis():    
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eyes_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:   
        return ""
    
def new_diagnosis_status():
    name = input(name_prompt)
    diagnosis = run_diagnosis()
    save_new_diagnosis(name, diagnosis)

def main():     
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            new_diagnosis_status()
        elif selection == "q":
            return

#main()


def test_assess_skin():
    print("Test Assess Skin")
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("3") == "")

test_assess_skin()

def test_assess_eyes():
    print("Test Assess Eyes")
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("3") == "")

test_assess_eyes()

def test_run_diagnosis():
    print("Test Run Diagnosis")
    print(run_diagnosis())

test_run_diagnosis()

#Project Completed.