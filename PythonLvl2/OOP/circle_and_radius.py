import math

class Circle:
    radius = 6
    def get_area(self):
        area = math.pi * self.radius**2
        print("Total are is:", area)
        return area
    

my_circle = Circle()
my_circle.get_area()