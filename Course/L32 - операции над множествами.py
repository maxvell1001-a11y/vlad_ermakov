# Задание 1:

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
#
# res = A & B # пересечение
# print(res)
# res = A | B # объединение
# print(res)
# res = A - B # разность A - B
# print(res)
# res = B - A # разность B - A
# print(res)
# res = A ^ B # симметрическая разность
# print(res)

# Задание 2:

# X = {10, 20, 30, 40, 50}
# Y = {30, 40}
#
# res = Y < X
# print(res)
# res = X > Y
# print(res)

# Задание 3:

# even_numbers = {2, 4, 6, 8, 10}
# odd_numbers = {1, 3, 5, 7, 9}
#
# print(even_numbers & odd_numbers) # пересечение, пустое множество
# print(even_numbers | odd_numbers) # объединение, все числа
#
# res = even_numbers | odd_numbers
# print(even_numbers < res) # проверка на подмножество

# Задание 4:

# python_students = {"Анна", "Иван", "Мария", "Сергей"}
# java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
#
# res = python_students & java_students
# print(res) # записаны на оба курса

# res = python_students ^ java_students
# print(res) # записаны только на один курс

# res = python_students | java_students
# print(res) # записаны хотя бы на один курс

# Задание 5:

text1 = set("программирование")
text2 = set("автоматизация")

print(text1.intersection(text2)) # общие буквы в двух словах
print(text1.difference(text2)) # буквы из первого, которых нет во втором
print(text1.symmetric_difference(text2)) # уникальные буквы для каждого слова