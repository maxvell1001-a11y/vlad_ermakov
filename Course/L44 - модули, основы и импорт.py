# Задание 1:

import math

print(math.sqrt(144))
print(math.pi)

# Задание 2:

from math import sqrt, pow

print(sqrt(64))
print(pow(5, 3))

# Задание 3:

import random

print("Случайное число:", random.randint(1, 10))
print("Выбранный язык:", random.choice(["Python", "Java", "C++"]))

# Задание 4:

import my_module

print(my_module.add(3, 5))
print(my_module.multiply(4, 6))

# Задание 5:

from utils import greet

greet("Алексей")

# Задание 6:

import time

start = time.time()
time.sleep(2)  # Задержка 2 секунды
end = time.time()

print(f"Код выполнялся {end - start:.4} сек") # (:.4) 4 знака после запятой