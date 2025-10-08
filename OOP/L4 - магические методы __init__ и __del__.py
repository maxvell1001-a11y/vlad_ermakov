# Задание 1:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")

    def __del__(self):
        print(f"Удалён объект: {self.name}")

p = Person('Петр', 25)
p.show_info()

# Задание 2:

# def __del__(self):
#     print(f"Удалён объект: {self.name}")  # Добавлено в классе Person

del p # срабатывает __del__: Удалён объект: Петр

# Задание 3:

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r1 = Rectangle()
print(f"Площадь прямоугольника: {r1.area()}")

r1 = Rectangle(2, 5)
print(f"Площадь прямоугольника: {r1.area()}")