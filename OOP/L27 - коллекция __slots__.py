# Задание 1: Сравнение с __dict__

class UserDict:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserSlots:
    __slots__ = ('name', 'email')

    def __init__(self, name, email):
        self.name = name
        self.email = email


user1 = UserDict('user1', '<EMAIL>')
user2 = UserSlots('user2', '<EMAIL>')

print(user1.__dict__)
print(hasattr(user2, '__dict__'))

# Задание 2: Ошибка при добавлении нового атрибута

class UserSlots:
    __slots__ = ('name', 'email')

    def __init__(self, name, email):
        self.name = name
        self.email = email

user2 = UserSlots('user2', '<EMAIL>')

# user2.phone = "+7..." # Ошибка

# Задание 3: Замер времени и памяти

from sys import getsizeof
from timeit import timeit

class A:
    def __init__(self):
        self.x = 1
        self.y = 2

class B:
    __slots__ = ('x', 'y')

    def __init__(self):
        self.x = 1
        self.y = 2

a = A()
b = B()

print(getsizeof(a.__dict__))
print(getsizeof(b)) # Меньше, чем в случае с __dict__

print("A time:", timeit(lambda: A(), number=100_000))
print("B time:", timeit(lambda: B(), number=100_000))