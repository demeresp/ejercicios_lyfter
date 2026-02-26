import actions


def main_menu():
    while True: 
        print("Welcome to the student-control system by Emers!")

        try:
            options = (input("""Please, type the option you would like to follow:
                    To add an student. 1

                    To see how many of students you currently have. 2

                    To see the general average of your students. 3

                    To see the best 3 sudents you have. 4
                             
                    To delete a student. 5
                             
                    To check unapproved students. 6
                    
                    To close the program. 7
                            
                        
                        :   """    , ).strip())
            if options == "1":
                    actions.add_student()
                    continue
            elif options == "2":
                    actions.student_list()
                    continue
            elif options == "3":
                    actions.all_students_average()
                    continue
            elif options == "4":
                    actions.best_3_avrg()
                    continue
            elif options == "5":
                actions.delete_students()
                continue
            elif options == "6":
                actions.unapproved_students()
                continue
            elif options == "7":
                print("Closing the program, see you later!")
                break

        except (ValueError):
            print("Make sure you are only typing the numbers 1, 2, 3, 4, 5 or 6")
            continue