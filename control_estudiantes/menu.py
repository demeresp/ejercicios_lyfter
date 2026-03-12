import actions
import data_ex_im

def main_menu():

    route_to_work_with = None

    students_to_add = None

    while True: 
        print("Welcome to the student-control system by Emers!")
        try:
            options = int(input("""Please, type the option you would like to follow:
                                
                        To import an specific route (recommended first). 1
                                
                        To enter students information. 2
                                
                        To save the students added. 3

                        To see how many of students you currently have. 4

                        To see the general average of your students. 5

                        To see the best 3 sudents you have. 6
                        
                        To check unapproved students. 7
                        
                        To close the program. 8
                        
                            
                            :   """    , ).strip())
            if options == 1:
                route_to_work_with = data_ex_im.route_validator()
                print("Working on:", route_to_work_with)
                continue
            elif options == 2:
                students_to_add = actions.n_student_dictionary()
                continue
            elif options == 3:
                current_students = data_ex_im.file_reader(route_to_work_with)
                if not students_to_add:
                        print("Please add some student(s) at the 2nd option back in the menu")
                        continue
                elif not route_to_work_with:
                        print("You have not provided a route to work, please specify a file route first")
                        continue
                else:
                    verifier = actions.duplicates_validator(students_to_add, current_students)                   
                if verifier:
                    print("Please try another grade/name")
                    continue
                else:
                    current_students.extend(students_to_add)
                    for stud in students_to_add:
                        data_ex_im.student_saver(route_to_work_with, stud)
                    print(f"Added {len(students_to_add)} student(s).")  
                continue
            elif options == 4:
                if route_to_work_with is None:
                    print("To display a list of students, load a file first (option 1)")
                    continue
                else:
                    actions.student_list(route_to_work_with)
                    continue
            elif options == 5:
                if route_to_work_with is None:
                    print("To display a list of students, load a file first (option 1)")
                    continue
                actions.all_students_average(route_to_work_with)
                continue
            elif options == 6:
                if route_to_work_with is None:
                    print("To display a list of students, load a file first (option 1)")
                    continue
                actions.best_3_avrg(route_to_work_with)
                continue
            elif options == 7:
                if route_to_work_with is None:
                    print("To display a list of students, load a file first (option 1)")
                    continue
                actions.unapproved_students(route_to_work_with)
                continue                
            elif options == 8:
                print("Closing the program, see you later!")
                break
            else:
                print("Please, only type numbers between 1-8")
                continue
        except ValueError:
                print("You only may type numbers (1-8)")
        except KeyboardInterrupt:
            print("Getting out of the program due to a keyborad interruption, see you later")
            break
