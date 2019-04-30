"""
    1. Create a Triangle Class.
    The class should have internal attributes which should not be access from outside (private). They should be able to hold the length of each of the 3 sides.
    You should implement a method that return the area of the triangle.
    You should implement properties for each of the attributes,

   Protocols
    2. Enable your Triangle class to
    Add another triangle to it. (tri1 + tri2). what should come out of this is up to you.
    The triangle should be able to tell its state, and it should be able to tell its length
"""
import math


class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def get_area(self):
        semi_parameter = (self.__a + self.__b + self.__c) / 2
        return math.sqrt((semi_parameter *
                          (semi_parameter - self.__a) *
                          (semi_parameter - self.__b) *
                          (semi_parameter - self.__c)))

    def __add__(self, other):
        self.__a += other.__a
        self.__b += other.__b
        self.__c += other.__c

    def __repr__(self):
        return f'Side a: {self.__a}\n' \
            f'Side b: {self.__b}\n' \
            f'Side c: {self.__c}\n' \
            f'Area: {self.get_area()}'


if __name__ == '__main__':
    triangle = Triangle(2, 2, 3)
    print(triangle)

    triangle_other = Triangle(3, 2, 2)

    triangle.__add__(triangle_other)

    print(triangle)
