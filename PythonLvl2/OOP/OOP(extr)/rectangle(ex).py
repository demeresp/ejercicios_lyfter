class Rectangle:
    
    width = 10
    height = 33
        


    def get_area(self):
        if self.width < 0 or self.height < 0:
            print("Width and height must be positive integers.")
            return None
        try:
            return self.width * self.height
        except ValueError:
            print("Please enter valid integers for width and height.")



    def get_perimeter(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("Width and height must be positive integers.")

        try:
            return 2 * (self.width + self.height)
        except ValueError:
            print("Please enter valid integers for width and height.")


my_rectangle = Rectangle()
my_rectangle.width = -1
print("Area of the rectangle:", my_rectangle.get_area())
print("Perimeter of the rectangle:", my_rectangle.get_perimeter())