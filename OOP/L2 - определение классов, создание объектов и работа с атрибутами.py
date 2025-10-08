# Задание 1:

class Dog:
    "Класс для описания собак"
    species = "canis"
    legs = 4

d1 = Dog()
d2 = Dog()

d1.legs = 3

print(d1.legs) # 3
print(d2.legs) # 4
print(d1.__dict__) # {'legs': 3}
print(d2.__dict__) # {}

# Задание 2:

print(Dog.__doc__) # Класс для описания собак

d1.name = "Бобик"
d1.age = 5

del d1.name
print(d1.__dict__) # {'legs': 3, 'age': 5}

try:
    print(d1.name) # пробуем обратиться к атрибуту name, которого нет
except AttributeError:
    print("Атрибут name больше не существует")

# Задание 3:

class User:
    role = "guest"
    active = True

setattr(User, "role", "admin") # изменение атрибута "role" на "admin"
print(User.role)

print(hasattr(User, "active")) # наличие атрибута "active" - True

setattr(User, "email", False) # создание атрибута "email" с значением False

delattr(User, "role") # удаление атрибута "role"
print(hasattr(User, "role")) # False

print(User.__dict__)