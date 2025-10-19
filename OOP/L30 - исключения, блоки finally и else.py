# Задание 1: Обработка деления с блоком else

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("Деление на ноль!")
# else:
#     print(f"Результат деления: {res}")

# Задание 2: Работа с finally

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError:
#     print("Деление на ноль!")
# else:
#     print(f"Результат деления: {res}")
# finally:
#     print("Работа программы завершена")

# Задание 3: finally и возврат из функции

def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Деление на ноль!")
        return None
    finally:
        print("Программа завершена")

safe_result = safe_divide(10, 2)
print(safe_result)

# Задание 4: Вложенные try/except

# try:
#     x, y = map(int, input().split())
#     try:
#         res = x / y
#     except ZeroDivisionError:
#         print("Деление на ноль!")
#     else:
#         print(f"Результат деления: {res}")
# except ValueError:
#     print("Неверный ввод!")

# Задание 5: Вложенные try через функцию

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "На ноль делить нельзя"

try:
    x, y = map(int, input().split())
    result = divide(x, y)
except ValueError:
    print("Ошибка ввода данных")
else:
    print("Результат деления:", result)