
def student_name():
        name_student = input("Type student name:",).split()
        for l in name_student:
            if l.isdigit():
                print("Valid names only have letters")
                continue
        return name_student



def grad_student():
    while True:
        student_grade = input("What is the student's grade?",)
        grades =  ["1A", "2B", "3C", "4D", "5C"]
        if student_grade not in grades:
            print("That grade does not exist yet...")
            print(grades)
            continue
        return student_grade



def student_notes():
    while True:
        try:
            spanish, english, history, sciences = [float(input(f"{note}: ")) 
            for note in ["spanish", "english", "history", "sciences"]]
        except (ValueError, TypeError):
            print("This should be only numbers")
            continue
            
        if any(note > 100 or note < 0 for note in [spanish, english, history, sciences]):
            print("Numbers should be less than 100 and bigger than 0")
            continue

        notes = {"spanish": spanish,
                "english": english,
                "history": history, 
                "sciences": sciences}


        return notes



def new_student():
    s_name = student_name()
    grad_stud = grad_student()
    notes_stud = student_notes()

    student = {
    "grade": grad_stud,
    "name": s_name,
    **notes_stud #El **notes_dict es el "unpack" de Python q mete todas las claves-valor del dict de notas dentro del dict del estudiante sin tener que escribirlas una por una.
    }

    return student



def all_students_average(notes):
    if not notes:
        return 0.0
    
    spanish = notes["spanish"]
    english = notes["english"]
    history = notes["history"]
    sciences = notes["sciences"]

    avrg = (spanish + english + history + sciences) / 4

    return avrg
















