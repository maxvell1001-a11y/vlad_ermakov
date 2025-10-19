# Задание 1: Ловим деление на ноль

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

# Задание 2: Обработка неверного ввода

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Ошибка ввода: введите два числа через пробел")

# Задание 3: Перехват всех исключений

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Ошибка ввода: введите два числа через пробел")
# except Exception:
#     print("Произошла неизвестная ошибка")

# Задание 4: Работа с объектом ошибки

try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception:
    print("Произошла неизвестная ошибка")

# Задание 5: Использование иерархии исключений

try:
    x, y = map(int, input().split())
    res = x / y
except ArithmeticError:
    print("Арифметическая ошибка")

# Задание 6: Блок except без типа ошибки

try:
    x, y = map(int, input().split())
    res = x / y
except:
    print("Возникла ошибка")

# Такой код ловит вообще все ошибки, в том числе системные
# ( KeyboardInterrupt , MemoryError ) —
# и скрывает важные проблемы, которые не стоит просто игнорировать.
# Лучше всегда указывать конкретные типы ошибок.