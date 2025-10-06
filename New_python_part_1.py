# IDE - интергрированная среда разработки
# DRY - Don't Repeat Yourself

# Числа

#  % - остаток от деления
#  // - целочисленное деление
#  ** - возведение в степень

flat_number = 24

entrance_number = (flat_number -1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print(entrance_number)
print(floor_number)

# Условные операторы

year = 2003

if not year % 4 and year % 100:
    print ("Year is leap")
elif not year % 400:
    print ("Year is leap")
else:
    print ("Year is not leap")

# Строки

big_integer = 2 ** 1000
print(len(str(big_integer)))

my_string = " Alice  "
print(my_string.upper()) # переводит в верхний регистр
print(my_string.lower()) # переводит в нижний регистр
print(my_string.strip()) # удаляет пробелы в начале и конце строки
print(my_string.replace(' ', '_')) # заменяет пробелы на _
print(my_string.count('A')) # подсчитывает количество символов
print(my_string.isdigit()) # проверяет, является ли строка числом
print(my_string.isalpha()) # проверяет, является ли строка буквами

name = "Alice"
age = 25
print(f"Hello, my name is {name} and I'm {age} years old")

# my_string = input ("Enter a number: ")
#
# if my_string.isdigit():
#     my_integer = int(my_string)
#     print(my_integer)
# else:
#     print(f"{my_string} is not a number")

print("Name: {name}, Age: {age}".format(name="Alice", age=25)) # метод format
print("Привет, %s! Тебе %d лет." % ("Анна", 25)) # форматирование через %

# Списки

fruit = ["apple", "banana", "cherry"]

print("apple" in fruit)

word = "apple"
my_list = list(word)
print(my_list) # ['a', 'p', 'p', 'l', 'e']

fruits = ["apple", "banana", "orange"]
fruits.append("watermelon")
print(fruits)
fruit = fruits.pop()
print(fruit) # watermelon - последний элемент списка
print(fruits) # ['apple', 'banana', 'orange']

fruits.extend(fruits) # добавляет все элементы списка в конец
fruits.reverse() # переворачивает список

my_list = [61, 122, 31]
my_list.sort(reverse=True) # - сортирует список по возрастанию
print(my_list, my_list[1])

my_string = "Alice cool man"
my_list = my_string.split(' ')
print(my_list) # ['Alice', 'cool', 'man'] - разбивает строку по пробелам

joined_string = ' '.join(my_list)
print(joined_string) # Alice cool man - соединяет элементы списка в строку

my_list = [61, 122, 31, 1, 0]
print(max(my_list))
print(min(my_list))
print(sum(my_list))

# Индексы и срезы

fruits = ["apple", "banana", "cherry"]

print(fruits[0]) # apple
fruits[0] = "pear" # изменяет элемент списка на "pear
print(fruits)
fruits[0], fruits[1] = fruits[1], fruits[0] # меняет местами элементы списка
print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num_new = numbers[2:10:2]
print(num_new) # [3, 5, 7, 9]

string = "Hello, world!"
print(string[:5]) # Hello

# Три способа развернуть список (list)
num = [1, 2, 3, 4, 5]

print(num[::-1]) # 1
num.reverse() # 2
new_num = list(reversed(num)) # 3

# Цикл for

file_name = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

for file in file_name:
    print(file) # выводит все элементы списка по очереди с каждой итерацией

greetings = "Hello, world!"
count_o = 0
char: str
for char in greetings:
    if char == "o":
        count_o += 1
        print(char)
print(count_o)

students = ["Alice", "Bob", "Charlie", "Dave"]

for student in students:
    print(student, end=" ")
    for char in student:
        print(char, end=" ")

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
    if num == 5:
        break
    print(num)

range_object = range(10)
print(range_object) # range(0, 10)

numbers = list(range_object)
print(numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [11, 12, 13, 14, 15]

for i in range(len(numbers)):
    numbers[i] += 1

print(numbers)

greeting = "Hello, world!"

indexes = []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        indexes.append(i)
        count += 1
print(indexes) # [4, 7, 10]
print(count) # 3

# Функции
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [11, 12, 13, 14, 15]


def find_average(numbers):
    average = sum(numbers) / len(numbers)
    return average


average_1 = find_average(numbers_1)
average_2 = find_average(numbers_2)
print(average_1, average_2)


def nothing():
    pass

nothing()


def format_date(*, day: int, month: str) -> str:
    return f"The date is {day} of {month}."


print(format_date(day=15, month="October"))  # Outputs: The date is 15 of October.


def custom_greeting(*, name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(custom_greeting(name="John"))  # Outputs: Hello, John
print(custom_greeting(name="John", greeting="Good morning"))  # Outputs: Good morning, John


# Область видимости переменных (локальных и глобальных)

DEFAULT_LEVEL_EXP = 200

def is_level_up(*, current_exp: int, gained_exp: int) -> bool:
    total_exp = current_exp + gained_exp
    level_up = False

    if total_exp >= DEFAULT_LEVEL_EXP:
        level_up = True

    return level_up

print(is_level_up(current_exp=150, gained_exp=60))  #True
print(is_level_up(current_exp=10, gained_exp=60))  #False

# Цикл while

counter = 1

while counter <= 5:
    print(f"Counter is {counter}") # выводит 5 раз
    counter += 1

my_list = [1, 2, 3]

while my_list:
    element = my_list.pop()  # удаляет последний элемент
    print(element)

print(my_list)

# while True:
#     print("Infinite loop")  # бесконечный цикл

# Кортежи

user_roles = ("admin", "moderator", "user")

role_1, role_2, role_3 = user_roles
print(role_1, role_2, role_3) # Распаковка кортежа, также можно и со списками

# Словари

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

person["job"] = "Developer" # добавляет новый элемент в словарь
print(person)

print(person["name"]) # выводит значение по ключу
print(person.get("country")) # выводит значение по ключу, если ключа нет, то выводит "Unknown".

for item in person.items():
    print(item)
    print(type(item)) # выводит кортеж

for key, value in person.items():
    print(key, value) # выводит ключ и значение, можно поотдельности

another_dict = {"name": "Alice", "age": 25}

person.update(another_dict) # добавляет новые элементы из другого словаря в текущий
person = person | another_dict # добавляет новые элементы из другого словаря в текущий
print(person)

# Функции со множеством элементов (*args и **kwargs)

def add_all(*args):
    print(args)
    print(type(args)) # выводит кортеж

add_all(1, 2, 3)

def introduce(**kwargs):
    print(kwargs) # именованные аргументы
    print(type(kwargs)) # выводит словарь

introduce(name="John", age=30)
introduce(**person) # распаковывает словарь в именованные аргументы