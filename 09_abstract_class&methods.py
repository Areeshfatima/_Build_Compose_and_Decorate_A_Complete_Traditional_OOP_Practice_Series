# Abstract Classes and Methods

from abc import ABC, abstractmethod   # module abc

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        # Abstract method: must be defined in child class
        pass

# Concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Implementation of abstract method
        return self.length * self.width
    
# Creating an object of Rectangle
rect = Rectangle(8, 12)

# Printing the area using implemented method
print("Area of Rectangle:", rect.area())
