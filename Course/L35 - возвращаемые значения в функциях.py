# Задание 1:

def add(a, b):
    return a + b


print(add(3, 7))

# Задание 2:

def is_positive(num):
    return True if num >= 0 else False


print(is_positive(5))
print(is_positive(-3))

# Задание 3:

def get_max(a, b, c):
    return max(a, b, c)

print(get_max(10, 25, 7))

# Задание 4:

def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Ошибка: деление на ноль"
    else:
        return "Ошибка: неизвестная операция"

print(calculate(10, 5, "+"))
print(calculate(10, 5, "*"))

# Задание 5:

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))