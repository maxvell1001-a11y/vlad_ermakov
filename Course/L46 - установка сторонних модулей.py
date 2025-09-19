# Задание 1:

import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Должно вывести 200

# Задание 2:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # Должно вывести: [ 2  4  6  8 10]

# Задание 3:

# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 50]
#
# plt.plot(x, y, marker='o')
# plt.title("Пример графика")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()

# Задание 4:

# pip freeze > requirements.txt
# pip uninstall requests
# pip install -r requirements.txt

# Задание 5:

# pip list
# pip install --upgrade numpy

# Задание 6:

import sys
import pprint

pprint.pprint(sys.path)

# Задание 7:

# pip uninstall matplotlib
# import matplotlib.pyplot as plt #ModuleNotFoundError: No module named 'matplotlib'