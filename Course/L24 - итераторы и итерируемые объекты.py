d = [5, 3, 7, 10, 32]
it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = "hello"

it = iter(d)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

def is_iterable(obj):
    try:
        iter(obj)  # Пробуем создать итератор
        return True
    except TypeError:  # Если возникает ошибка, значит, объект не итерируемый
        return False

# Тестируем функцию
print(is_iterable([1, 2, 3]))  # True (список)
print(is_iterable("abc"))      # True (строка)
print(is_iterable(42))         # False (число)
print(is_iterable({1, 2, 3}))  # True (множество)