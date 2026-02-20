import data_ex_im
import actions

import csv

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



def add_student():
    while True:
        print("Type the new student information:")
        current_students = data_ex_im.file_reader(r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
        s_name = actions.student_name()
        grade = actions.grad_student()
        verifier = any(student["name"].strip().lower() == s_name.strip().lower() and student["grade"].upper().lower() == grade for student in current_students)
                                    #ignoro mayus y minus para que no se caiga en caso de haber, asimismo strip para evitar espacios (que no deberia haber pero doble refuerzo)
        if verifier:
            print("That student name + grade already exists, please use a second name or add it to a different grade!")
            continue
        

        notes_stud = actions.student_notes()

        new_stud = {
        "grade": grade,
        "name": s_name,
        **notes_stud #El **notes_dict es el "unpack" de Python q mete todas las claves-valor del dict de notas dentro del dict del estudiante sin tener que escribirlas una por una.
        }
        saver_student = data_ex_im.student_saver(new_stud, r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
        return saver_student
 


def all_of_them_average():
    reader = data_ex_im.file_reader(r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
    calc = actions.all_students_average(reader)
    print(f"""The general average for current students is: 
                        {calc} """)
    return calc



def best_3_avrg():
    reader = data_ex_im.file_reader(r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
    calc = actions.best_3_avrg(reader)
    print("Current top averages:", calc)
    return calc



def delete_student():
    reader = data_ex_im.file_reader(r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
    new_list = actions.delete_student(reader)
    saver = data_ex_im.file_saver(new_list, r"C:\Users\demer\OneDrive\Desktop\ejercicios_lyfter\control_estudiantes\data_students.csv")
    return new_list

