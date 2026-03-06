import actions
import data_ex_im

def main_menu():
    try:
        route_to_work_with = data_ex_im.route_validator()
    except FileNotFoundError:
        print("Error while loading this file, please try with other o check for typos")
        return
    while True: 
        print("Welcome to the student-control system by Emers!")
        try:
            options = int(input("""Please, type the option you would like to follow:
                        To add an student. 1

                        To see how many of students you currently have. 2

                        To see the general average of your students. 3

                        To see the best 3 sudents you have. 4
                        
                        To check unapproved students. 5
                        
                        To close the program. 6
                        
                            
                            :   """    , ).strip())
            if options == "1":
                    actions.add_student(route_to_work_with, route_to_work_with)
                    continue
            elif options == "2":
                    actions.student_list(route_to_work_with)
                    continue
            elif options == "3":
                    actions.all_students_average(route_to_work_with)
                    continue
            elif options == "4":
                    actions.best_3_avrg(route_to_work_with)
                    continue
            elif options == "5":
                actions.unapproved_students(route_to_work_with)
                continue
            elif options == "6":
                print("Closing the program, see you later!")
                break
            else:
                print("Please, only type numbers between 1-7")
                continue
        except ValueError:
                print("You only may type numbers (1-7)")
        except KeyboardInterrupt:
            print("Getting out of the program due to a keyborad interruption, see you later")
        except Exception as error:
            print("Unexpected issue, hoing back...")
        continue
