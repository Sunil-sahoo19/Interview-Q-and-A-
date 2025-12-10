from abc import ABC, abstractmethod

class Shape(ABC):
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 
rect = Rectangle(12, 10)
print(rect.area())  # Output: 120