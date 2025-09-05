# Задание 1

# d = {"Беларусь": "Минск", "Россия": "Москва", "Китай": "Пекин"}

# d.setdefault("Япония", "Токио")
# print(d)

# res = d.get(input("Введите страну: "))
# if res:
#     print(res)
# else:
#     print("Такой страны нет")

# Задание 2

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
#
# min_student = min(grades, key=grades.get)
# grades.pop(min_student)
# print(grades)

# Задание 3

# students = [["Анна", 20], ["Борис", 22], ["Виктор", 19], ["Галина", 21]]
#
# d = dict.fromkeys([name for name, _ in students], None)
# print(d)
#
# d.update(dict(students))
# print(d)

# Задание 4:

# exchange_rates = {"USD": 90, "EUR": 98, "GBP": 115}
#
# input_currency = input("Введите валюту: ")
#
# if input_currency in exchange_rates:
#     print(exchange_rates[input_currency])
# else:
#     print("Неизвестная валюта")
#
# exchange_rates.setdefault("BYN", 10)
# print(exchange_rates)

# Задание 5:

dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}

dict1.update(dict2)
print(dict1)