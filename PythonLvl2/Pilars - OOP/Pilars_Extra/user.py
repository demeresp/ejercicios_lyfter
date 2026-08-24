from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    @abstractmethod
    def get_role(self):
        pass


    @abstractmethod
    def has_permission(self, permission):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"


    def has_permission(self, permission):
        return True
    


class RegularUser(User):
    def get_role(self):
        return "Regular User"


    def has_permission(self, permission):
        return permission in ["read", "write"]



user1 = Admin("Mbappe", 30)
user2 = RegularUser("Alvaro", 25)