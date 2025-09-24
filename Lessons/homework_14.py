# 1. Импортируйте только функции sqrt и pow из модуля math и вычислите:

from math import sqrt, pow

print(sqrt(64))
print(pow(5, 3))

# 2. Импортируйте модуль random

import random

import random

print("Случайное число:", random.randint(1, 10))
print("Выбранный язык:", random.choice(["Python", "Java", "C++"]))

# 3. Создайте свой модуль my_module.py, в котором будут функции:

import my_module

print(my_module.add(3, 5))
print(my_module.multiply(4, 6))

# 4. Создайте два Python-файла:

import main

# 5. Напишите программу, которая измеряет время выполнения кода с помощью time.sleep(2), используя модуль time.

import time

start = time.time()
time.sleep(2)  # Задержка 2 секунды
end = time.time()

print(f"Код выполнялся {end - start:.4} сек") # (:.4) 4 знака после запятой

# 6. Установите библиотеку requests и проверьте, работает ли она.

import requests

response = requests.get("https://www.google.com")
print(response.status_code)

# 7. Установите библиотеку matplotlib и постройте график.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# plt.plot(x, y, marker='o')
# plt.title("Пример графика")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# 8. Создайте requirements.txt с зависимостями вашего проекта.

# pip freeze > requirements.txt
# pip uninstall requests
# pip install -r requirements.txt

# 9. Создание простого пакета

import math_operations

print(math_operations.add(1, 2))
print(math_operations.subtract(1, 2))