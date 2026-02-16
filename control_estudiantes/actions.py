
def student_name():
        name_student = input("Type student name:",).strip()
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



def all_students_average(students_list):
    if not students_list:
        return 0.0
    
    av_sum = 0.0
    
    for student in students_list:
        try:
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            sciences = float(student["sciences"]) # convertir a float pa que no trate como strings lo que trae CSV, si trata como lista *keyerror
            avrg = (spanish + english + history + sciences) / 4
            av_sum += avrg
        except (KeyError, TypeError):
            print("Error processing student data")
            continue

        result = av_sum / len(students_list)
    
    return result



def best_3_avrg(students_list):
    if not students_list:
        return []
    
    avrg_list = []
    
    for student in students_list:
        try:
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            sciences = float(student["sciences"])
            avrg = (spanish + english + history + sciences) / 4  #le sumo el nombre para que no se pierda la referencia a qué estudiante corresponde cada promedio, sino solo tendría los promedios sin saber a quién pertenecen
            avrg_list.append((avrg, student["name"])) #lo guardo como tupla para que el orden se mantenga, si lo guardara como lista se perderia la referencia entre el promedio y el nombre al ordenar por promedio
        except (KeyError, TypeError):
            print("Error processing student data")
            continue

    best_3 = sorted(avrg_list, reverse=True)[:3]
    
    return best_3














