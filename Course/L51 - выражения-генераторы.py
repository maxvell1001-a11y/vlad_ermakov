# Задание 1:

gen = (x ** 2 for x in range(10))

print(next(gen))
print(next(gen))
print(next(gen))

# Задание 2:

gen = (x ** 2 for x in range(10))

for num in gen:
    if num % 2 == 0:
        print(num)

# Задание 3:

gen = (x for x in range(101))

print(sum(gen))

# Задание 4:

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

gen = fib(10)
for num in gen:
    print(num, end=" ")

# Задание 5:

gen = (x for x in range(1000000))

for num in gen:
    print(num, end=" ")
    if num > 10:
        break

# Задание 6:

lst = ["Python", 123, "Java", 456, "C++", 789]

gen = (x for x in lst if type(x) == str)

for num in gen:
    print(num, end=" ")

# Задание 7:

import random

gen = (random.randint(1, 100) for _ in range(10))

print(max(gen))

# Задание 8:

with open("words.txt", "r", encoding="utf-8") as file:
    gen = (word for word in file.read().split() if len(word) > 5)
    print(" ".join(gen))