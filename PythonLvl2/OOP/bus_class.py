class Person:

    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):                                                      #despues de self>atributos q tendre q dar
        self.max_passengers = max_passengers
        self.passengers = []
    

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"One {person.name} passenger just got into the bus") #llamar el nombre mediante el parametro conocido por la funcion en este caso 'person que contiene 'name 
        else:
            print("The bus is full")

    
    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"One {person.name} is out of the bus now")
        else:
            print(f"{person.name} is not in this bus")


koala = Person("Koala")
bus = Bus(max_passengers=15)
bus.add_passenger(koala)
Amarillo = Person("Amarillo")
bus.add_passenger(Amarillo)  