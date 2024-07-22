
from math import pi
class Figure:

    def area(self):
        raise NotImplementedError("The area method must be implemented in a subclass")

    def perimeter(self):
        raise NotImplementedError("The perimeter method must be implemented in a subclass")


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class EquilateralTriangle(Figure):
    def __init__(self, basis, height):
        self.basis = basis
        self.height = height

    def area(self):
        return (self.basis * self.height) / 2

    def perimeter(self):
        return self.basis * 3


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)


square = Square(5)
rectangle = Rectangle(4, 6)
equilateral_triangle = EquilateralTriangle(3, 4)
circle = Circle(7)

figures = [square, rectangle, equilateral_triangle, circle]

for figure in figures:
    print(f"Figure: {type(figure).__name__}\n"
          f"Area: {figure.area()}\n"
          f"Perimeter: {figure.perimeter()}\n")