import csv
import data_ex_im
import keyboard #$ py -m pip install keyboard pa instalar esta libreriab 


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
        print("Please digit the scores for this student (spanis, english, histoy sciences)....")
        try:
            spanish, english, history, sciences = [float(input(f"{note}: ")) 
            for note in ["spanish", "english", "history", "sciences"]]
        except (ValueError, TypeError):
            print("This should be only numbers")
            continue
            #true si algo se cumple para que no siga el program :0, viva any!
        if any(note > 100 or note < 0 for note in [spanish, english, history, sciences]):
            print("Numbers should be less than 100 and bigger than 0")
            continue

        notes = {"spanish": spanish,
                "english": english,
                "history": history, 
                "sciences": sciences}


        return notes



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



def delete_student(students_list):
    if not students_list:
        return None
    

    while True:
        try:
            name_to_delete = input("Please type the student you would delete or type a number to exit:",).split()
            if int in name_to_delete:
                break

            for student in students_list:
                if name_to_delete in students_list:
                    des = input(f"Are you sure you would like to delete this student: {name_to_delete} forever? y / n :", ).split()
                    if "y" in des:
                        student.clear()
                        print("Student has been successfully removed")
                        break
                    elif "n" in des:
                        print("Going back...")
                        break
                elif name_to_delete not in students_list:
                    print("That name is not an active student")
                    continue

        except(ValueError, TypeError):
            print("Make sure you are not typing any numbers or spaces")
            continue
        return students_list


def student_list():
        try:
            print("Loading current students list...")
            grades = data_ex_im.file_reader(r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
            amount_of_students = len(grades)
            if isinstance(grades, list):
                print(f"""These are the current students: (Amount : {amount_of_students}) 
                
                            {grades} """)
                
        except FileNotFoundError as Nofile:
            print("The file provided is not foundable")
        return grades



def student_gen_info():
    while True:
        print("Please type the student information you are adding or 'TAB' to go back....")
        if keyboard.is_pressed('tab'): 
            print("Getting out")
            break
        while True:
            s_name = student_name()
            grade = grad_student()
                #verifier = any(student["name"].strip().lower() == s_name.strip().lower() and student["grade"].upper().lower() == grade for student in current_students)
            notes_stud = student_notes()                            #ignoro mayus y minus para que no se caiga en caso de haber, asimismo strip para evitar espacios (que no deberia haber pero doble refuerzo)
        
            new_stud = {
        "grade": grade,
        "name": s_name,
        **notes_stud #El **notes_dict es el "unpack" de Python q mete todas las claves-valor del dict de notas dentro del dict del estudiante sin tener que escribirlas una por una.
            }
            continue
    return new_stud




student_gen_info()


