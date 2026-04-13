import data_ex_im
from student_builder import Student


def student_object():
        stage_of_students = []
        while True:
            s_name = student_name()
            s_grade = grad_student()
            notes_stud = student_notes()

            new_stud = Student(s_name, s_grade, notes_stud)

            verifier  = any(
                stud.name.strip().lower() == s_name.strip().lower() and
                stud.grade.strip().upper() == s_grade.strip().upper() for stud in stage_of_students)
            if verifier:
                print(f"Student {s_name}, {s_grade} is already on the list, please set it in another grade")
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



def best_3_avrg(route):
            
    if not route:
        print("Please provide a route to read first. (Option 1.)")
        return False

    students_list = data_ex_im.file_reader(route)
    if not students_list:
        print("The current file is empty, please add students to work with")
        return False
            
    avrg_list = []
            
    for student in students_list:
        try:
            avrg_list.append((student.get_average(), student.name, student.grade))
        except (KeyError, TypeError):
            print("Error processing student data")
            continue
        best_3 = sorted(avrg_list, reverse=True)[:3]
    return best_3



def unapproved_students(route):

        if not route:
            print("You have not provided a file to read yet, please go back to option 1.")
            return False

        students_list = data_ex_im.file_reader(route)
        if not students_list:
            print("The current file is empty, please add students to work with")
            return False

        unapproved = []
        
        for student in students_list:
            try:
                if not student.is_approved():
                    unapproved.append((student.name, student.grade, student.get_average()))
            except (KeyError, TypeError):
                print("Error processing student data")
                continue
        
        return unapproved



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
        print("Please digit the scores for this student (spanish, english, histoy sciences)....")
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

        if not route:
            print("Please provide a route to read first. (Option 1.)")
            raise FileNotFoundError

        students_list = data_ex_im.file_reader(route)
        if not students_list:
            print("The current file is empty, please add students to work with")
            return False

        av_sum = 0.0
        
        for student in students_list:
            try:
                av_sum += student.get_average()
            except (KeyError, TypeError):
                print("Error processing student data")
                continue

        result = av_sum / len(students_list)
        
        return result



def duplicates_validator(new_students, current_students):
    for new in new_students:
        
        verifier = any(
            stud.name.strip().lower() == new.name.strip().lower() and
            stud.grade.strip().upper() == new.grade.strip().upper() for stud in current_students
        )
    if verifier:
        print(f"Student(s), {new.name}, ({new.grade}) already exists....")
        return True
    elif not verifier:
            pass



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
                    
                print(f"{i}. {student.name} (Grade: {student.grade})") 
                    
        except FileNotFoundError as Nofile:
            print("The file provided is not foundable")
        return grades