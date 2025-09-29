# Задание 1:

nums = [4, 3, -10, 1, 7, 12]
nums.sort()

a = sorted(nums, key=lambda x: x % 2)
print(a)

# Задание 2:

words = ["груша", "апельсин", "банан", "яблоко", "киви"]

res = sorted(words, key=len)
print(res)

# Задание 3:

names = ["петр", "Иван", "мария", "Анна"]

res = sorted(names)
print(res)

# Задание 4:

cities = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]

res = sorted(cities, key=lambda x: x[-1])
print(res)

# Задание 5:

products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]

res = sorted(products, key=lambda x: x[1])
print(res)

# Задание 6:

books = [
("Евгений Онегин", "Александр Пушкин"),
("Муму", "Иван Тургенев"),
("Мастер и Маргарита", "Михаил Булгаков"),
("Мертвые души", "Николай Гоголь")
]

res = sorted(books, key=lambda x: x[1].split()[-1])
print(res)