from abc import ABC, abstractmethod

# Interface
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Circle class
class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r


# Rectangle class
class Rectangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


# Object creation
c = Circle(5)
r = Rectangle(4, 6)

print("Circle Area =", c.area())
print("Rectangle Area =", r.area())