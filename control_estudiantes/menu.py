import main

def main_menu():
    while True: 
        print("Welcome to the student-control system by Emers!")
        try:
            options = (input("""Please, type the option you would like to follow:
                    To add an student. 1

                    To see how many of students you currently have. 2

                    To see the general average of your students. 3

                    To see the best 3 sudents you have. 4 
                    
                    To close the program. 5 
                        -"""    , ).strip())
        
            if "1" in options:
                add = main.add_student()
            elif "2" in options:
                verify = main.student_list()
            elif "3" in options:
                verify = main.all_of_them_average()
            elif "4" in options:
                best = main.best_3_avrg()
            elif "5" in options:
                print("Thanks for using the system, see you later!")
                break
            elif "6" in options:
                delete = main.delete_student()
    
        except ValueError as error:
            print("You should select only numbers")



main_menu()