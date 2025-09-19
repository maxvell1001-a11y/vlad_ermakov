# Задание 1:

import math_utils

print(math_utils.square(3))
print(math_utils.cube(2))

# Задание 2:

from string_utils import capitalize_words, reverse_string

print(capitalize_words("hello world"))
print(reverse_string("Python"))

# Задание 3:

import random_utils

print(random_utils.random_choice(["Python", "Java", "C++"]))

# Задание 4:

import my_module

# Задание 5:

import test_module # Не выполняется, т.к. не запускается напрямую

# Задание 6:

import sys
import pprint

pprint.pprint(sys.path)

# Задание 7:

import reload_test
import importlib

importlib.reload(reload_test)  # Перезагрузка модуля, отображается ещё раз