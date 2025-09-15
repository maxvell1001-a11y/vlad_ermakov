# 1. Привет, <name>! Добро пожаловать!

def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")

greet("Анна")

# 2. Напишите функцию square(num), которая принимает число и возвращает его квадрат.

def square(num):
    result = num ** 2
    return result

print(square(5))

# 3. Создайте функцию is_even(num), которая возвращает True, если число четное, и False, если нечетное.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))

# 4. Напишите функцию repeat_string(text, times), которая повторяет строку text times раз.

def repeat_string(text, times):
    i = text * times
    return i

print(repeat_string("Python", 3))

# 5. Напишите функцию add(a, b), которая принимает два числа и возвращает их сумму.

def add(a, b):
    result = a + b
    return result

print(add(3, 7))

# 6. Напишите функцию get_max(a, b, c), которая возвращает максимальное из трех чисел.

def get_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(get_max(10, 25, 7))

# 7. Создайте функцию calculate(a, b, operation), которая выполняет одну из операций:

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))

# 8. Создайте функцию reverse_string(text), которая принимает строку и возвращает её в обратном порядке.

def reverse_string(text):
    result = text[::-1]
    return result

print(reverse_string("Python"))

# 9. Создайте функцию compare_strings(s1, s2, ignore_case=True, ignore_spaces=True),
# которая сравнивает две строки, убирая пробелы и регистр, если соответствующие параметры установлены в True.

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1 = s1.lower()
        s2 = s2.lower()
    if ignore_spaces:
        s1 = s1.replace(" ", "")
        s2 = s2.replace(" ", "")
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))

# 10. Напишите функцию summarize(*args), которая возвращает сумму всех переданных чисел.

def summarize(*args):
    return sum(x for x in args if isinstance(x, (int, float)))

print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))

# 11. Напишите функцию create_profile(name, age, **extra),
# которая принимает имя, возраст и дополнительные параметры

def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    if extra:
        print("Дополнительная информация:")
        for key, value in extra.items():
            print(f"  {key}: {value}")

create_profile("Иван", 30, city="Москва", job="Инженер")

# 12. Напишите функцию process_orders(*orders, discount=0),
# которая принимает список заказов (чисел) и применяет скидку.

def process_orders(*orders, discount=0):
    total = sum(orders)
    discounted_total = total * (1 - discount / 100)
    print(f"Сумма заказа: {total}")
    print(f"С учетом скидки: {discounted_total}")

process_orders(100, 200, 300, discount=10)

# 13. Создайте функцию merge_lists(*lists), которая объединяет несколько списков в один.

def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    return result

print(merge_lists([1, 2], [3, 4], [5, 6]))

# 14. Создайте функцию merge_dicts(*dicts), которая объединяет несколько словарей в один.

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}

print(merge_dicts(d1, d2, d3))