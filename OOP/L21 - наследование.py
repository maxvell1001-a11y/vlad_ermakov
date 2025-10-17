# Задание 1: Классы Shape , Circle , Square

from math import pi

import math

import requests


class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

c = Circle(5)
s = Square(4)
print(c.area())
print(s.area())

# Задание 2: Классы страниц BasePage , LoginPage

class BasePage:
    def open(self, url):
        print(f"Открытие страницы: {url}")

class LoginPage(BasePage):
    def login(self, username, password):
        print(f"Ввод логина: {username}")
        print(f"Ввод пароля: {password}")
        print("Нажатие на кнопку 'Войти'")

page = LoginPage()
page.open("https://example.com/login")
page.login("user", "1234")


# Задание 3: Примитивы рисования

class Primitive:
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        pass

class Line(Primitive):
    def draw(self):
        print(f"Рисуем линию от ({self.x1}, {self.y1}) до ({self.x2}, {self.y2})")

class Rect(Primitive):
    def draw(self):
        print(f"Рисуем прямоугольник от ({self.x1}, {self.y1}) до ({self.x2}, {self.y2})")

p1 = Line()
p2 = Rect()

p1.set_coords(1, 2, 3, 4)
p2.set_coords(1, 2, 3, 4)

p1.draw()
p2.draw()