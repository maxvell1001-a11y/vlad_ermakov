# Задание 1:

names = ["Андрей", "Сергей", "Мария", "Екатерина"]
ages = [25, 30, 22, 28]

result = zip(names, ages)
print(list(result))

# Задание 2:

students = ["Анна", "Виктор", "Павел"]
scores = [85, 92, 78]
subjects = ["Математика", "Физика", "Информатика"]

result = zip(students, scores, subjects)
print(list(result))

# Задание 3:

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

result = [x * y for x, y in zip(a, b)]
print(result)

# Задание 4:

colors = ["красный", "синий", "зеленый"]
objects = ["яблоко", "ручка", "трава", "небо"]

result = zip(colors, objects)
print(list(result))

# Задание 5:

countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]

result = dict(zip(countries, capitals))
print(result)

# Задание 6:

data = [(1, 'a'), (2, 'b'), (3, 'c')]

t1, t2 = zip(*data)
print(list(t1),list(t2))

# Задание 7:

names = ["Иван", "Петр", "Ольга"]
scores = [80, 90, 75]
subjects = ["Математика", "Физика", "Химия"]

result = [f"{name} получил {score} баллов по {subject}" for name, score, subject in zip(names, scores, subjects)]
print(result)