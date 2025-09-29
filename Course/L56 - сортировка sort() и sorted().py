# Задание 1:

nums = [42, 1, 56, -7, 12, 99, 3]

nums.sort()
print(nums)

# Задание 2:

result = sorted(nums, reverse=True)
print(result)

# Задание 3:

words = ["яблоко", "груша", "апельсин", "банан", "киви"]

words.sort()
print(words)
res = sorted(words, key=len)
print(res)

# Задание 4:

students = [("Анна", 22), ("Иван", 19), ("Мария", 21), ("Петр", 18)]

res = sorted(students)
res2 = sorted(students, key=lambda x: x[1])
print(res)
print(res2)

# Задание 5:

grades = {"Анна": 85, "Иван": 92, "Мария": 78, "Петр": 90}

res = sorted(grades)
print(res)
res2 = sorted(grades, key=grades.get, reverse=True)
print(res2)

# Задание 6:

products = [
{"name": "Телефон", "price": 500},
{"name": "Ноутбук", "price": 1000},
{"name": "Планшет", "price": 700}
]

res = sorted(products, key=lambda x: x["price"])
print(res)
res = sorted(products, key=lambda x: x["price"], reverse=True)
print(res)

# Задание 7:

names = ["петр", "Иван", "мария", "Анна"]

res = sorted(names, key=lambda x: (x[0].isupper(), x.lower()))
print(res)