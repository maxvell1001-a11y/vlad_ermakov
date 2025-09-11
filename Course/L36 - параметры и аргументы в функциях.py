# Задание 1:

def power(base, exp=2):
    return base ** exp


print(power(3))
print(power(3, 3))

# Задание 2:

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

print(greet("Анна"))
print(greet("Анна", "Добро пожаловать"))

# Задание 3:

def rectangle_area(a=1, b=1):
    return a * b

print(rectangle_area())
print(rectangle_area(5))
print(rectangle_area(4, 3))

# Задание 4:

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()
    if ignore_spaces:
        s1, s2 = s1.strip(), s2.strip()
    return s1 == s2

print(compare_strings("Hello", " hello "))
print(compare_strings("Hello", "HELLO", ignore_case=False))
print(compare_strings("Hello ", "Hello", ignore_spaces=False))

# Задание 5:

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst


print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3, [10, 20]))