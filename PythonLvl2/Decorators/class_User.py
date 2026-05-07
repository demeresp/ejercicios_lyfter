from datetime import date

class User:
    def __init__(self, date_of_b):
        self.date_of_b = date_of_b

    @property
    def age(self):
        today = date.today
        return today.year - self.date_of_b
    

def if_adult(fun):
    def wrapper(*args):
        for num in args:
            if num < 18:
                raise ValueError("You are not an adult")
        return fun(*args)
    return wrapper


@if_adult
def register_user(user):
    return f"Welcome {user}!"


user1 = register_user(25)