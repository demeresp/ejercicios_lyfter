from datetime import datetime

class FinanceGestor:

    def __init__(self):
            self.available_spent_categories = ['entertainment', 'education', 'transportation']
            self.movements = []


    def validate_spent_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        elif amount < 0:
            raise ValueError("Amount spent must be more than 0")
        else:
            return amount


    def declare_description(self, description):
        if len(description) > 20:
            raise IndexError("Description can take up to 20 caracthers, please add a brief description")
        else:
            return description


    def date_validation(self, date_given):
        try:
            selected_date = datetime.strptime(date_given, "%d/%m/%Y")
            if selected_date > datetime.now():
                raise ValueError("Date cannot be in the future")
            return selected_date.strftime("%d/%m/%Y")
        except ValueError as e:
            raise ValueError("Invalid date format, please use d/m/y")


    def add_category(self, new_category):
            if new_category not in self.available_spent_categories:
                self.available_spent_categories.append(new_category)
            else:
                raise ValueError("Category already exists")


    def add_income(self, title, category, date, amount):
        if category not in self.available_spent_categories:
            raise ValueError("Category does not exists, please add it first!")

        title = self.declare_description(title)
        amount = self.validate_spent_amount(amount)
        category = self.add_category(category)
        date = self.date_validation(date)

        new_movement = Movement(title=title,
                                amount=amount,
                                category = category,
                                movement_type="income",
                                date=date)

        self.movements.append(new_movement)


    def add_expense(self, title, category, date, amount):
        if category not in self.available_spent_categories:
            raise ValueError("Category does not exists, please add it first!")

        title = self.declare_description(title)
        amount = self.validate_spent_amount(amount)
        category = self.add_category(category)
        date = self.date_validation(date)

        new_movement = Movement(title=title,
                                amount=amount,
                                category=category,
                                date=date,
                                movement_type="expense")

        
        self.movements.append(new_movement)


    def obtain_all_movements(self):
        return self.movements 


    def only_get_incomes(self):
        return [mov for mov in self.movements if mov.movement_type == "income"]


    def only_get_expenses(self):
        return [mov for mov in self.movements if mov.movement_type == "expense"]



class Movement:

    def __init__(self, title, category, date, movement_type, amount):

        self.title = title
        self.category = category
        self.date = date
        self.movement_type = movement_type
        self.amount = amount


    def movements_to_dict(self):

        return {"title":self.title,
                "category":self.category,
                "date":self.date,
                "amount":self.amount,
                "movement_type":self.movement_type
                }


    @classmethod
    def from_dict_to_object(cls, data):
        return cls(
            title=data["title"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            movement_type=data["movement_type"]
        )



