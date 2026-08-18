import FreeSimpleGUI as sg
from logic_src_main import FinanceGestor as fgr, Movement as mvm
from persistance_files_managment import DataManager as dm

def open_add_expense_window(gestor, data_manager):

    categories = gestor.available_spent_categories

    
    layout_expense = [
        [sg.Text("Add Expense")],
        [sg.Text("Title:"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Text("Date (dd/mm/yyyy):"), sg.Input(key="-DATE-")], #readonly=True → el usuario no puede escribir, solo elegir
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    window_expense = sg.Window("Add Expense", layout_expense)

    while True:
        event_ex, values_ex = window_expense.read()

 

        if event_ex == "Save":
            title = values_ex["-TITLE-"].strip()
            amount_str = values_ex["-AMOUNT-"].strip()
            category = values_ex["-CATEGORY-"].strip().lower() 
            date = values_ex["-DATE-"].strip()


        if title == "" or amount_str == "" or category == "" or date == "":
            sg.popup_error("Spaces cannot be in blank")
            continue

        try:
            amount = float(amount_str)
        except ValueError:
            sg.popup_error("Amount must be a number")


        try:
            category = category.strip().lower()
            gestor.add_expense(title, category, date, amount)
            data_manager.save_movements(gestor.obtain_all_movements(), r"data/movements.json")
            sg.popup("Expense added successfully!")
            break
        except Exception as e:
            sg.popup_error(str(e))


    window_expense.close()


def open_add_income_window(gestor, data_manager):

    categories = gestor.available_income_features

    layout_income = [
    [sg.Text("Add Income")],
    [sg.Text("Title:"), sg.Input(key="-TITLE-")],
    [sg.Text("Amount:"), sg.Input(key="-AMOUNT-")],
    [sg.Text("Category:"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
    [sg.Text("Date (dd/mm/yyyy):"), sg.Input(key="-DATE-")],
    [sg.Button("Save"), sg.Button("Cancel")]]

    income_window = sg.Window("Add Income", layout_income)

    while True:

        event_in, value_in = income_window.read()

        if event_in == "Save":
                    title = value_in["-TITLE-"].strip()
                    amount_str = value_in["-AMOUNT-"].strip()
                    category = value_in["-CATEGORY-"].strip().lower() 
                    date = value_in["-DATE-"].strip()

        if event_in == sg.WINDOW_CLOSED or event_in == "Cancel":
            break

        if title == "" or amount_str == "" or category == "" or date == "":
            sg.popup_error("Spaces cannot be in blank")
            continue

        try:
            amount = float(amount_str)
        except ValueError:
            sg.popup_error("Amount must be a number")


        try:
            gestor.add_income(title, category, date, amount)
            data_manager.save_movements(gestor.obtain_all_movements(), r"data/movements.json")      
            sg.popup("Income added successfully!")
            break
        except Exception as e:
            sg.popup_error(str(e))

    income_window.close()


def add_income_category(gestor, data_manager):

    new_category = None

    category_layout = [[sg.Text("Add Income Category")],
                        [sg.Text("What new category you would like to add to the list?"), sg.Input(key="-NEW_CATEGORY-")],
                        [sg.Button("Save"), sg.Button("Cancel")]]

    category_window = sg.Window("Add category", category_layout)

    while True:
        event_cat, value_cat = category_window.read()

        if event_cat == "Save":
            new_category = value_cat["-NEW_CATEGORY-"].strip().lower()

        if event_cat == sg.WIN_CLOSED or event_cat == "Cancel":
            break

        if new_category == "":
            sg.popup_error("Category cannot be None, add one or go back!")
            continue


        try:
            gestor.add_income_category(new_category)
            sg.popup("Category added to the list!")
            break
        except Exception as e:
            sg.popup_error (str(e))

    category_window.close()


def add_expense_category(gestor, data_manager):

    new_category = None

    category_layout = [[sg.Text("Add Expense Category")],
                        [sg.Text("What new category you would like to add to the list?"), sg.Input(key="-NEW_CATEGORY-")],
                        [sg.Button("Save"), sg.Button("Cancel")]]

    category_window = sg.Window("Add category", category_layout)

    while True:
        event_cat, value_cat = category_window.read()

        if event_cat == "Save":
            new_category = value_cat["-NEW_CATEGORY-"].strip().lower()

        if event_cat == sg.WIN_CLOSED or event_cat == "Cancel":
            break

        if new_category == "":
            sg.popup_error("Category cannot be None, add one or go back!")
            continue


        try:
            gestor.add_expense_category(new_category)
            sg.popup("Category added to the list!")
            break
        except Exception as e: 
            sg.popup_error (str(e))

    category_window.close()


def show_movements_table(gestor, data_manager):
    movements = gestor.obtain_all_movements()

    data = []
    for mov in movements:
        data.append([mov.title,
                    mov.amount,
                    mov.category,
                    mov.date,
                    mov.movement_type])


    layouts_movement = [
            [sg.Text("-LIST OF MOVEMENTS-")],
                        [sg.Table(values=data,
                                headings=["Title", "Amount", "Category", "Date", "Type"],
                                key="-MOVEMENTS-TABLE-",
                                auto_size_columns=True,
                                justification = "left",
                                num_rows = 15)],
                                [sg.Button("Close")]
                                ]

    window = sg.Window('Movements', layouts_movement)

    while True:
        event_mov, value_mov = window.read()
        if event_mov == sg.WIN_CLOSED or event_mov == "Close":
            break

    window.close()




main_layout = [[sg.Text("Welcome to your FinancialAdmin!")],
            [sg.Button('Add Expense'), sg.Button("Add Income")],
            [sg.Button('Add Income Category')],
            [sg.Button('See Movements')],
            [sg.Button('Add Expense Category')],
            #[sg.Input(key='-INPUT-')],
            #[sg.Button('Add Expense'), sg.Button('Add income')],
            [sg.Button('Ok'), sg.Button('Quit')]]

    # Create the window
window = sg.Window('FinancialAdminbyEmer', main_layout)

gestor = fgr()
data_manager = dm()

gestor.movements = data_manager.load_movements(r"data/movements.json")

    # Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
        # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == "Add Expense":
        open_add_expense_window(gestor, data_manager)
    if event == "Add Income":
        open_add_income_window(gestor, data_manager)
    if event == "Add Income Category":
        add_income_category(gestor, data_manager)
    if event == "Add Expense Category":
        add_expense_category(gestor, data_manager)
    if event == "See Movements":
        show_movements_table(gestor, data_manager)
        
window.close()
