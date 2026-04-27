class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    
    def get_info(self):
        return f"Vehicle Description: {self._brand}, {self._year},"
    

class Car(Vehicle):
    def __init__(self, brand, year, doors, color, kind):
        super().__init__(brand, year)
        self.doors = doors
        self.color = color
        self.kind = kind

    def get_info(self):
        return f"Car Description: {self._brand}, {self._year}, {self.doors}, {self.color}, {self.kind}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, kind, color, speed):
        super().__init__(brand, year)
        self.kind = kind
        self.color = color
        self.speed = speed

    def get_info(self):
        return f"Motorcycle Description: {self._brand}, {self._year}, {self.kind}, {self.color}, {self.speed}"
    


nissan = Car("Nissan", 2020, 4, "Red", "Sedan")
print(nissan.get_info())

honda = Motorcycle("Honda", 2018, "Sport", "Blue", "200 km/h")
print(honda.get_info())