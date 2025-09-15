# 1. Создайте множество с элементами

set_1 = {1, "2", "wdwe", 16.5, 12}

set_1.add(333333)
set_1.update(["223"])
set_1.update([333333]) # Уже есть, не добавит

print(set_1)

# 2. Создайте множество из списка городов:

cities = {"Moscow", "London", "Paris", "Berlin", "London"}

print(len(cities)) # 4, London второй раз не добавится

# 3. Создайте множество с числами от 1 до 10.

set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set_2.remove(5)
set_2.discard(15)

print(set_2)

# 4. Преобразуйте строку "abrakadabra" в множество символов.

set_3 = set("abrakadabra")

print(set_3)
print(len(set_3))

# 5. Создайте пустое множество и попробуйте добавить в него следующие элементы:

set_4 = set()

set_4.add(10)
set_4.add("hello")
# set_4.add((1, 2, 3)) # Кортеж, нельзя добавить
# set_4.add([4, 5, 6]) # Список, нельзя добавить

print(set_4)

# 6. Создайте 2 множества, в которых совпадают 2 элемента

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

set_5 = A & B
set_6 = A | B
set_7 = A - B
set_8 = B - A
set_9 = A ^ B

print(set_5, set_6, set_7, set_8, set_9, sep="\n")

# 7. Создайте два множества из чисел 1 до 10:

A = {2, 4, 6, 8, 10}
B = {1, 3, 5, 7, 9}

print(A & B) # Пустое множество
print(A | B) # Все числа

# 8. Даны множества студентов, записавшихся на курсы:

python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}

print(python_students.intersection(java_students)) # Студенты, записавшиеся на оба курса
print(python_students.difference(java_students)) # Студенты, записавшиеся только на Python
print(java_students.intersection(python_students)) # Студенты, записавшиеся только на Java
print(python_students.union(java_students)) # Студенты, записавшиеся хотя бы на один курс

# 9. Даны множества слов:

text1 = set("программирование")
text2 = set("автоматизация")

print(text1.intersection(text2))
print(text1.difference(text2))
print(text1.symmetric_difference(text2))

# 1. Создайте множество из квадратов чисел от 1 до 10, но только для четных чисел.

set_10 = {i ** 2 for i in range(1, 11) if i % 2 == 0}
print(set_10)

# 2. Дан список:

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]

new_set = {word.upper() for word in set(words)}
print(new_set)

# 3. Дан словарь:

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}

a = {name: "отлично" if score >= 80 else "удовлетворительно" for name, score in grades.items()}
print(a)

# 4. Дано множество слов:

text = {"Python", "automation", "programming", "testing"}

new_dict = {name: len(name) for name in text}
print(new_dict)

# 5. Создайте вложенный словарь

n = 10

dict_1 = {n: {i: i ** 2 for i in range(1, 11)} for n in range(1, 11)}
for key, value in dict_1.items():
    print(f"{key}: {value}")