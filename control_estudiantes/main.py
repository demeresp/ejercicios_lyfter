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
    print("Type the new student information:")
    new_stud = actions.new_student() #unicamente contiene estudiante
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
    calc = actions.all_students_average(reader)
    best_3 = sorted(calc, reverse=True)[:3]
    print("Current top averages:", best_3)
    return best_3

