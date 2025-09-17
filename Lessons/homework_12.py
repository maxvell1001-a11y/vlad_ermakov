# 1. Создайте lambda-функцию, которая возвращает квадрат числа.

sqrt = lambda x: x ** 2
print(sqrt(5))

# 2. Создайте lambda-функцию, которая проверяет, является ли число четным.

iven = lambda x: x % 2 == 0
print(iven(5))

# 3. Используйте lambda в sorted(), чтобы отсортировать список строк по последней букве.

words = ["banana", "apple", "cherry"]

sort_by_last_letter = sorted(words, key=lambda word: word[-1])

print(sort_by_last_letter)

# 1. Создайте функцию multiply_by(n), которая принимает число n и возвращает вложенную функцию.
# Вложенная функция должна принимать число x и возвращать его произведение на n.

def multiply_by(n):
    def inner(x):
        return x * n

    return inner

times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))
print(times5(10))

# 2. Напишите функцию counter(start=0), которая возвращает вложенную функцию.
# Каждый вызов вложенной функции должен увеличивать счетчик на 1.

def counter(start=0):
    def inner():
        nonlocal start
        start += 1
        return start
    return inner

c1 = counter(5)
c2 = counter()

print(c1())
print(c1())
print(c2())
print(c2())