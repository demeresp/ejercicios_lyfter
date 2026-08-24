
class Animal:
    def __init__(self, name):
        self.name = name


    def speak(self):
        return print(" *makes a sound* ")


class Dog(Animal):

    def speak(self):
        return "Guau!"
        


class Cat(Animal):

    def speak(self):
        return "Miau!"



dog1 = Dog("Toby")
print(dog1.speak())


cat1 = Cat("Jonsu")
print(cat1.speak())