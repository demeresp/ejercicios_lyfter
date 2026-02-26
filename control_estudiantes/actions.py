
import data_ex_im 


def student_name():
        name_student = input("Type student name:",).strip()
        for l in name_student:
            if not name_student or any(l.isdigit() for l in name_student):
                print("Make sure you are only typing letters and that the name is not empty")
                return student_name()
        return name_student



def grad_student():
    while True:
        student_grade = input("What is the student's grade?",).strip().upper()
        if len (student_grade) in [2, 3] and student_grade[:-1].isdigit() and student_grade[-1].isalpha():
            return student_grade
        else:
            print("Make sure that you are following this format: '1A', '2B', '3C'...9D and that the grade is not empty")
            continue


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



def all_students_average(route=None):
    route = data_ex_im.route_validator()
    students_list = data_ex_im.file_reader(route)
    
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

    print(f"The general average of all students is: {result:.2f}") #:.2f para mostrar solo 2 decimales, puede usarse 3, 4... lo que se quiera, es un formato para mostrar el resultado de forma pro
    
    return result



def best_3_avrg(route=None):
    route = data_ex_im.route_validator()
    students_list = data_ex_im.file_reader(route)
    
    avrg_list = []
    
    for student in students_list:
        try:
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            sciences = float(student["sciences"])
            avrg = (spanish + english + history + sciences) / 4  #le sumo el nombre para que no se pierda la referencia a qué estudiante corresponde cada promedio, sino solo tendría los promedios sin saber a quién pertenecen
            avrg_list.append((avrg, student["name"], student["grade"])) #lo guardo como tupla para que el orden se mantenga, si lo guardara como lista se perderia la referencia entre el promedio y el nombre al ordenar por promedio
        except (KeyError, TypeError):
            print("Error processing student data")
            continue

    best_3 = sorted(avrg_list, reverse=True)[:3]
    print("The best 3 students are:")
    for avrg, name, grade in best_3:
        print(f"{name} (Grade: {grade}) with an average of {avrg:.2f}")
    
    return best_3



def student_list(route=None):
        
        try:
            print("Loading current students list...")
            route = data_ex_im.route_validator()
            grades = data_ex_im.file_reader(route) #splitlines para que cada estudiante quede en una línea diferente, sino quedaría todo como un string gigante y no se podría mostrar de forma ordenada
            amount_of_students = len(grades)
            print("The total amount of students is:", amount_of_students)
            for i, student in enumerate(grades, start=1): #segundo i indica donde empezara enumerate
                
                print(f"{i}. {student['name']} (Grade: {student['grade']})") 
                
        except FileNotFoundError as Nofile:
            print("The file provided is not foundable")
        return grades



def n_student_dictionary():
    stage_of_students = []
    while True:
        s_name = student_name()
        grade = grad_student()
        notes_stud = student_notes()

        new_stud = {
            "grade": grade,
            "name": s_name,
            **notes_stud
        }

        stage_of_students.append(new_stud)
        print(f"Student {s_name} has been successfully added to list of students to be added")
        try:
            des = input("Would you like to add another student? y / n:").strip().lower()
            if des == "y":
                continue
            elif des == "n":
                print("Going back...")
                break
        except TypeError:
            print("Make sure you are only typing y or n")
            continue

    return stage_of_students



def add_student(existing_students=None, new_students=None, n_route=None):

    if not n_route:
        n_route = data_ex_im.route_validator()
        if not n_route:
            print("The route cannot be empty, please provide a valid route")
            return None

    existing_students = data_ex_im.file_reader(n_route)
    while True:
        if new_students is None:
            new_students = n_student_dictionary()

        if not new_students:
            print("There are no new students to add, please add a student first")
            continue

        
        already_exists = any(
            s["name"].strip().lower() == new_students[0]["name"].strip().lower() and
            s["grade"].strip().upper() == new_students[0]["grade"].strip().upper()
            for s in existing_students
        )

        if already_exists:
            print(F"One or more students already exists in the current list, please check the information before adding")
            return None

        f_des = input(f"Are you sure you would like to add {len(new_students)} student(s)? y / n:").strip().lower()
        if f_des == "y":
            existing_students.extend(new_students)
            for student in new_students:
                data_ex_im.student_saver(n_route, student)
            print(f"Added {len(new_students)} student(s).")
            
            o_des = input("Would you like to add more students? y / n:").strip().lower()
            if o_des not in ["y", "n"]:
                print("Make sure you are only typing y or n")
                continue
            elif o_des == "y":
                new_students = None
                continue
            elif o_des == "n":
                print("Going back...")
                break
            else:
                print("Make sure you are only typing y or n")
                continue
        elif f_des == "n":
            print("Cancelled. Going back...")
            return None
        else:
            print("Make sure you are only typing y or n")
            continue



def unapproved_students(route=None):
    route = data_ex_im.route_validator()
    students_list = data_ex_im.file_reader(route)
    
    unapproved = []
    
    for student in students_list:
        try:
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            sciences = float(student["sciences"])
            avrg = (spanish + english + history + sciences) / 4
            if spanish < 60 or english < 60 or history < 60 or sciences < 60:
                unapproved.append((student["name"], student["grade"], student["spanish"], student["english"], student["history"], student["sciences"], avrg))
        except (KeyError, TypeError):
            print("Error processing student data")
            continue

    if unapproved:
        print("The unapproved students are:")
        for name, grade, spanish, english, history, sciences, avrg in unapproved:
            print(f"{name} (Grade: {grade}) with the following scores: Spanish: {spanish}, English: {english}, History: {history}, Sciences: {sciences} and an average of {avrg:.2f}")
    else:
        print("There are no unapproved students.")
    
    return unapproved


#def delete_students(route=None):

    route = data_ex_im.route_validator()
    students = data_ex_im.file_reader(route)

    while True:
        new_students = []
        if not students:
            print("There are no students to delete.")
            return None
        try:
            student_to_delete = input("Please, type the name of the student you want to delete:").strip()
            student_to_delete_grade = input("Please, type the grade of the student you want to delete:").strip().upper()
            des = input(f"Are you sure you want to delete {student_to_delete} from grade {student_to_delete_grade}? y / n:").strip().lower()
            if des == "y":
                pass
            elif des == "n":
                print("Cancelled. Going back...")
                return None
            student_exists = any(
                s["name"].strip().lower() == student_to_delete.strip().lower() and
                s["grade"].strip().upper() == student_to_delete_grade.strip().upper()
                for s in students
            ) 
            if not student_exists:
                print("The student you want to delete does not exist, please check the information and try again.")
                return None
            new_students = [s for s in students if not (s["name"].strip().lower() == student_to_delete.strip().lower() and s["grade"].strip().upper() == student_to_delete_grade.strip().upper())]
            new_file = data_ex_im.file_saver(new_students, route)
            print(f"Student {student_to_delete} from grade {student_to_delete_grade} has been successfully deleted.")
            o_des = input("Would you like to delete another student? y / n:").strip().lower()
            if o_des == "y":
                continue
            elif o_des == "n":
                    print("Going back...")
                    break
            else:
                    print("Make sure you are only typing y or n")
                    continue
        except ValueError:
            print("Make sure you are only typing letters for the name and a valid grade format (e.g., '1A', '2B', etc.)")
            continue
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error: {error}. Please provide a valid route and check your permissions.")
            continue
    return new_file