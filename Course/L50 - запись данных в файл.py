# Задание 1:

# with open('output.txt', 'r', encoding="utf-8") as file:
#     print(file.read())

# Задание 2:

# with open('output.txt', 'a+', encoding="utf-8") as file:
#     file.write("Python — это круто!\n")
#     print(file.read())

# Задание 3:

lines = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]

with open("lines.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

with open("lines.txt", "r", encoding="utf-8") as file:
    print(file.read())

# Задание 4:

try:
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        sum = 0
        for line in file:
            sum += int(line)
        print(sum)
except FileNotFoundError:
    print("Ошибка: Файл не найден")

# Задание 5:

# from datetime import datetime
#
# current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
# with open("log.txt", "a", encoding="utf-8") as file:
#     file.write(f"{current_time}\n")

# Задание 6:

import pickle

lst = ["яблоко", "банан", "апельсин"]

with open("data.bin", "wb") as file:
    pickle.dump(lst, file)

with open("data.bin", "rb") as file:
    loaded = pickle.load(file)
    print(loaded)

# Задание 7:

lines = ["Алексей 85\n", "Марина 90\n", "Иван 78\n"]

with open("students.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

with open("students.txt", "r", encoding="utf-8") as file:
    students = [line.strip().split() for line in file]
    best_student = max(students, key=lambda x: int(x[1]))
    print(f"Лучший студент: {best_student[0]} ({best_student[1]})")

# Задание 8:

with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Python — отличный язык программирования.\nЯ изучаю Python каждый день.")

with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()
    content = content.replace("Python", "Java")
with open("text.txt", "w", encoding="utf-8") as file:
    file.write(content)
    print(content)