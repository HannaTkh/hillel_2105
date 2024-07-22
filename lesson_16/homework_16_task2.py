from abc import ABC, abstractmethod

from math import pi


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figura):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class EquilateralTriangle(Figura):
    def __init__(self, basis, height):
        self.__basis = basis
        self.__height = height

    def area(self):
        return (self.__basis * self.__height) / 2

    def perimeter(self):
        return self.__basis * 3


class Circle(Figura):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(pi * self.__radius ** 2, 2)

    def perimeter(self):
        return round(2 * pi * self.__radius, 2)


square = Square(5)
equilateral_triangle = EquilateralTriangle(3, 4)
circle = Circle(7)

figures = [square, equilateral_triangle, circle]

for figure in figures:
    print(f"Figure: {type(figure).__name__}\n"
          f"Area: {figure.area()}\n"
          f"Perimeter: {figure.perimeter()}\n")
