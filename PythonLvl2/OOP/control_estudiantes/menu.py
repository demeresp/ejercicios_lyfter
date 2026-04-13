import actions
import data_ex_im


class Menu:

    def __init__(self):
        print("Welcome to the student control system!")
        self.route_to_work_with = None
        self.students_to_add = None


    def show_options_in_menu(self):
        return int(input("""
Please, select an option from the menu:
                        1. Load a file to work with
                        2. Enter students information
                        3. Save the students added
                        4. See how many students you currently have
                        5. See the general average of your students
                        6. See the best 3 students you have
                        7. Check unapproved students
                        8. Close the program
"""))

    
    def options_operator(self):
        while True:
            try:
                options = self.show_options_in_menu()
                if options == 1:
                    self.route_to_work_with = data_ex_im.route_validator()
                    print(f"You are now working with the file: {self.route_to_work_with}")
                elif options == 2:
                    if not self.route_to_work_with:
                        print("Please add a route to work first at option 1!")
                        continue
                    else:
                        self.students_to_add = actions.student_object()
                elif options == 3:
                    if not self.route_to_work_with:
                        print("Please add a route to work first at option 1!")
                        continue
                    if not self.students_to_add:
                        print("You must add some students first at option 2!")
                    else:
                        data_ex_im.file_saver(self.route_to_work_with, self.students_to_add)
                elif options == 4:
                    if not self.route_to_work_with:
                        print("You have not provided a file to read yet, please go back to option 1.")
                        continue
                    else:
                        students_list = data_ex_im.file_reader(self.route_to_work_with)
                        print(f"You currently have {len(students_list)} students in your file.")
                elif options == 5:
                    if not self.route_to_work_with:
                        print("You have not provided a file to read yet, please go back to option 1.")
                        continue
                    else:
                        students_list = data_ex_im.file_reader(self.route_to_work_with)
                        if students_list:
                            avrg = actions.general_average(students_list)
                            print(f"The general average of your students is: {avrg:.2f}")
                        else:
                            print("The current file is empty, please add students to work with")
                elif options == 6:
                    if not self.route_to_work_with:
                        print("You have not provided any file to get students, please check option 1")
                        continue
                    else:
                        best_3 = actions.best_students(self.route_to_work_with)
                        if best_3:
                            print("The best 3 students you have are:")
                            for avg, name, grade in best_3:
                                print(f"{name} from grade {grade} with an average of {avg:.2f}")
                        else:
                            print("All students are approved")
                        continue
                elif options == 7:
                    if not self.route_to_work_with:
                        print("You have not provided a file to read yet, please go back to option 1.")
                        continue
                    else:
                        unapproved = actions.unapproved_students(self.route_to_work_with)
                        if unapproved:
                            print("The unapproved students are:")
                            for name, grade, avg in unapproved:
                                print(f"{name} from grade {grade} with an average of {avg:.2f}")
                        else:
                            print("All students are approved")
                elif options == 8:
                    print("Closing the program, goodbye!")
                    break
                else:
                    print("Please, select a valid option from the menu.")
            except ValueError:
                print("Please, enter a number corresponding to the options in the menu.")
                continue
            except KeyboardInterrupt:
                print("\nProgram interrupted.")
                break