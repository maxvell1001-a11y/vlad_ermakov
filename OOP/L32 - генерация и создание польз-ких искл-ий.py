# Задание 1: Явный вызов стандартного исключения

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return x / y

print(divide(1, 2)) # 0.5
# print(divide(1, 0)) # ZeroDivisionError: Деление на ноль!

# Задание 2: Свой класс исключения

class NegativeNumberError(Exception):
    """Это исключение должно подниматься, если в функцию sqrt(x) передают
отрицательное число"""

def sqrt(x):
    if x == 0:
        raise NegativeNumberError("Нельзя извлечь корень из нуля!")
    return x

# sqrt(0) #NegativeNumberError: Нельзя извлечь корень из нуля!

# Задание 3: Применение пользовательского исключения

def sqrt(x):
    if x < 0:
        raise NegativeNumberError("Число должно быть положительным!")
    return x ** 0.5

try:
    sqrt(-1)
except NegativeNumberError as e:
    print(e)

# Задание 4: Иерархия пользовательских исключений

class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Деление на ноль!")
    return x / y

try:
    res = divide(1, 0)
except MathError as e:
    print(e)
else:
    print(f"Результат успешного деления: {res}")

# Задание 5: Применение в тестах
class NegativeNumberError(Exception):
    """Исключения с отрицательным числом"""
    pass

def sqrt(x):
    return x ** 0.5

def test_sqrt():
    try:
        sqrt(-9)
    except NegativeNumberError:
        assert False, "Нельзя брать корень из отрицательного числа"

test_sqrt()