## Unit B
## task 6.10.2
#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_name(self):
        return Rectangle.__name__

rect = Rectangle(5, 5)
print(F'Площадь {rect.get_name()}: {rect.get_area()}')