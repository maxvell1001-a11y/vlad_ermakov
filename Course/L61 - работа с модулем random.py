import random

# Задание 1:

a = (random.random() for _ in range(3))
print(list(a))

# Задание 2:

for _ in range(5):
    print(random.randint(-5, 5))

# Задание 3:

colors = ["red", "green", "blue", "yellow", "purple"]
a = random.choice(colors)
print(f"Выбран цвет: {a}")

# Задание 4:

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Задание 5:

data = [10, 20, 30, 40, 50, 60, 70]
a = random.sample(data, 3)
print(a)

# Задание 6:

random.seed(0)
print([random.randint(0, 100) for _ in range(10)])

# Задание 7:

for _ in range(5):
    print(random.gauss(0, 1))