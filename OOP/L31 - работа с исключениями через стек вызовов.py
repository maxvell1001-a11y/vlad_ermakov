# Задание 1: Исключение в глубокой функции

def inner():
    return 1 / 0

def outer():
    return inner()

# outer() # Ошибка, стек вызовов: line 4, in inner -> line 7, in outer

# Задание 2: Перехват исключения на верхнем уровне

def inner():
    return 1 / 0

def outer():
    try:
        return inner()
    except ZeroDivisionError:
        print("Ошибка перехвачена на верхнем уровне")

outer() # Ошибка перехвачена на верхнем уровне

# Задание 3: Локальная обработка в глубокой функции

def inner():
    try:
        return 1 / 0
    except ZeroDivisionError:
        print("Ошибка в inner")

def outer():
    return inner()

outer() # Ошибка в inner

# Задание 4: Обработка через разные уровни

def inner():
    return 1 / 0

def outer():
    try:
        return inner()
    except ZeroDivisionError:
        print("Ошибка в outer")

outer() # Ошибка в outer

# Задание 5: Применение в тесте

def get_value():
    return int(input("Введите число: "))

def test_get_value():
    try:
        return get_value()
    except ValueError as e:
        print(f"Ошибка: {e}")
        assert False, "Тест завершился неудачно из-за ValueError"

test_get_value()