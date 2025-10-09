# Задание 1:

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

print(Circle.is_valid_radius(500)) # True
print(Circle.is_valid_radius(1500)) # False

# Задание 2:

import math

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    def __init__(self, r):
        if self.is_valid_radius(r):
            self.r = r
        else:
            self.r = self.MIN_RADIUS

    @staticmethod
    def area(r):
        return math.pi * r ** 2

c = Circle(10)
print(c.area(c.r))

# Задание 3:

import math

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    def __init__(self, r):
        if self.is_valid_radius(r):
            self.r = r
        else:
            self.r = self.MIN_RADIUS

    @staticmethod
    def area(r):
        return math.pi * r ** 2

    def print_info(self):
        cls = type(self)
        print("Радиус:", self.r)
        print(f"Допустимы диапазон: [{self.MIN_RADIUS}, {self.MAX_RADIUS}]")

c = Circle(50)
c.print_info()