# Задание 1: Единый метод для разных классов

class Cat:
    def speak(self):
        return  'мяу'

class Dog:
    def speak(self):
        return 'гав'

class Duck:
    def speak(self):
        return 'кря'

animals = [Cat(), Dog(), Duck()]

for animal in animals:
    print(animal.speak())

# Задание 2: Абстрактный метод get_pr()

class Shape:
    def get_pr(self):
        raise NotImplementedError("Метод должен быть переопределён")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_pr(self):
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_pr(self):
        return 2 * (self.width * self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

shapes = [Square(5), Rectangle(2, 3), Triangle(1, 2, 3)]

for shape in shapes:
    print(shape.get_pr())

# Задание 3: Реализация абстрактного класса через

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_pr(self):
        return self.side * 4

# s = Shape() #`TypeError: Can't instantiate abstract class Shape with abstract methods get_pr

s2 = Square(5) # Всё ОК
print(s2.get_pr())