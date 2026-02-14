import csv

def new_name_student():
    try:
        stud_name = input("Type the student name:",).split()
    except ValueError as error:
        ("Please only type alphanumeric values")
        for name in stud_name:
            if "" in name:
                print("Please remove all the spaces here")
                continue
    return stud_name


def new_grade_student():
    try:
        grade_student = (input("Type the grade this person will be part of:",))
    except ValueError as error:
        ("You can only type numbers here")
        for grade in grade_student:
            if "" in grade: 
                print("Please remove all the spaces here")
                continue
    return grade_student


def student_notes():
    try:
        spanish, history, english, sciences = [int(input(f"{note}: ")) for note in ["spanish", "english", "history", "sciences"]]
    except ValueError as error:
        ("Debe ingresar un numero aqui!")

        notes = {
        "spanish": spanish,
        "english": english,
        "history": history,
        "sciences": sciences
            }
        
        return notes
    

def file_reader(route):
    with open(route, 'r', encoding="utf-8") as file:
        try:
            reader = csv.DictReader(file)
            if isinstance(reader, list):
                return reader
        except FileNotFoundError:
            print("The route/file provided is not valid")




