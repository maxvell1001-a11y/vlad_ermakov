# Задание 1: Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел.

a = { x ** 2 for x in range(1, 11) if x % 2 == 0 }
print(a)

# Задание 2:

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]

a = set(words)
a2 = {a.upper() for a in words}
print(a2)

# Задание 3:

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}

a = {name: "отлично" if score >= 80 else "удовлетворительно" for name, score in grades.items()}
print(a)

# Задание 4:

text = {"Python", "automation", "programming", "testing"}

text_new = {key: len(key) for key in text}
print(text_new)

# Задание 5:

nested = {n: {x ** 2 for x in range(1, n + 1)} for n in range(1, 6)}
print(nested)