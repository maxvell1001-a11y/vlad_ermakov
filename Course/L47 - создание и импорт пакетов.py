# Задание 1: Создание простого пакета

# from .addition import *
# from .subtraction import *

# Задание 2: Работа с вложенными пакетами

import geometry

print(geometry.circle_area(5))
print(geometry.rectangle_area(4, 6))

# Задание 3: Относительный импорт внутри пакета

import text_processing

text = "hello world! this is python."

print(text_processing.capitalize_text(text))
print(text_processing.count_words(text))

# Задание 4: Создание __all__ для ограничения импорта

from text_processing import *

print(capitalize_text("hello world!"))
# print(count_words("hello world!")) # Ошибка! (не импортировано)

# Задание 5: Проверка, запущен ли модуль напрямую

# if __name__ == "__main__":
#     print(capitalize_text("test string"))

# Задание 6: Повторный импорт с importlib.reload()

import text_processing
import importlib

print(text_processing.capitalize_text("hello python!"))

importlib.reload(text_processing) # Перезагрузка модуля