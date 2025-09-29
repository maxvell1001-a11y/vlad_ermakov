# Задание 1:

a = 42
b = 3.14
c = "Python"
d = False

for var in (a, b, c, d):
    print(isinstance(var, int), isinstance(var, float), isinstance(var, str), isinstance(var, bool))

# Задание 2:

data = (1.2, 3, "text", 5.7, True, [1, 2], 0.5)

s = sum(filter(lambda x: isinstance(x, float), data))
print(s)

# Задание 3:

s = sum(filter(lambda x: type(x) is int, data))
print(s)

# Задание 4:

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]

s = filter(lambda x: isinstance(x, (str, list)), items)
print(list(s))

# Задание 5:

def describe_type(x):
    if type(x) is bool:
        return print("Это булево значение")
    elif isinstance(x, (int, float)):
        return print("Это число")
    elif isinstance(x, str):
        return print("Это строка")
    else:
        return print("Неизвестный тип")

describe_type(5.5) # Это число
describe_type(True) # Это булево значение
describe_type("Привет") # Это строка
describe_type([1, 2, 3]) # Неизвестный тип