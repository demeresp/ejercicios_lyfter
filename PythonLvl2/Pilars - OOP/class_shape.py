from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    
    def calculate_perimeter(self):
        return 2 * self.radius * math.pi
    

    def calculate_area(self):
        return math.pi * self.radius**2
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    

    def calculate_area(self):
        return self.width * self.height



class square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length


    def calculate_perimeter(self):
        return 4 * self.side_length


    def calculate_area(self):
        return self.side_length**2


my_circle = Circle(5)
print("Circle perimeter:", my_circle.calculate_perimeter())
print("Circle area:", my_circle.calculate_area())

my_square = square(4)
print("Square perimeter:", my_square.calculate_perimeter())
print("Square area:", my_square.calculate_area())

my_rectangle = Rectangle(3, 5)
print("Rectangle perimeter:", my_rectangle.calculate_perimeter())
print("Rectangle area:", my_rectangle.calculate_area())

