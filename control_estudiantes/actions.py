
import data_ex_im


def student_name():
        name_student = input("Type student name:",).strip().upper()
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

    while True:
        if not route:
            print("Please provide a route to read first. (Option 1.)")
            raise FileNotFoundError

        students_list = data_ex_im.file_reader(route)
        if not students_list:
            print("The current file is empty, please add students to work with")

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



def best_3_avrg(route):
        
    while True:

        if not route:
            print("Please provide a route to read first. (Option 1.)")
            return False

        students_list = data_ex_im.file_reader(route)
        if not students_list:
            print("The current file is empty, please add students to work with")
        
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
    
    while True:
        if not route:
            print("Please provide a route to read first. (Option 1)")
            raise FileNotFoundError
            

        try:
            print("Loading current students list...")
            grades = data_ex_im.file_reader(route) 
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

        verifier  = any(
            stud["name"].strip().lower() == s_name.strip().lower() and
            stud["grade"].strip().upper() == grade.strip().upper() for stud in stage_of_students)
        if verifier:
            print(f"Student {s_name}, {grade} is already on the list, please set it in another grade")
            continue
        else:
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



def duplicates_validator(new_students, current_students):
    for new in new_students:
        

        verifier = any(
            stud["name"].strip().lower() == new["name"].strip().lower() and
            stud["grade"].strip().upper() == new["grade"].strip().upper() for stud in current_students
        )


    if verifier:
        print(f"Student(s), {new["name"]}, ({new["grade"]}) already exists....")
        return True
    elif not verifier:
            pass



def unapproved_students(route):

    if not route:
        print("You have not provided a file to read yet, please go back to option 1.")
        return False

    students_list = data_ex_im.file_reader(route)
    if not students_list:
        print("The current file is empty, please add students to work with")

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
