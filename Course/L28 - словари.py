# fruits = {
#     "яблоко": 120,
#     "банан": 90,
#     "апельсин": 150
# }
# fruits["груша"] = 100
#
# print(fruits)

# grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
#
# high_scores = [name for name, grade in grades.items() if grade >= 4]
# print(high_scores)

# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# capitals = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим"}
#
# a = input("Введите страну: ")
# print(capitals.get(a, "Неизвестная страна"))

students = [
    ("Анна", "Python"),
    ("Борис", "Java"),
    ("Виктор", "Python"),
    ("Галина", "C++"),
    ("Дмитрий", "Python")
]

courses = {}

for name, course in students:
    if course not in courses:
        courses[course] = []
    courses[course].append(name)

print(courses)