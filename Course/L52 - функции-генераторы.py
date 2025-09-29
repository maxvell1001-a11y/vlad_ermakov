# Задание 1:

def sqrt():
     for i in range(1, 10):
          yield i ** 2

gen = sqrt()

print(next(gen))
print(next(gen))
print(next(gen))

# Задание 2:

def even_numbers(start, end):
     for num in range(start, end + 1):
          if num % 2 == 0:
               yield num

for num in even_numbers(2, 12):
     print(num, end=" ")

# Задание 3:

def fibonacci(n):
     a, b = 0, 1
     for _ in range(n):
          yield a
          a, b = b, a + b

for num in fibonacci(10):
     print(num, end=" ")

# Задание 4:

def find_python_lines(filename):
     with open("text_2.txt", encoding="utf-8") as file:
          for line in file:
               if "Python" in line:
                    yield line.strip()

for line in find_python_lines("text_2.txt"):
     print(line)

# Задание 5:

# import random
#
# def random_generator():
#      while True:
#           i = random.randint(1, 100)
#           yield i
#           if i == 50:
#                break
#
# for num in random_generator():
#      print(num, end=" ")

# Задание 6:

# def prime_numbers(n):
#      count, num = 0, 2
#      while count < n:
#           if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#                yield num
#                count += 1
#                num += 1
#
# for num in prime_numbers(10):
#      print(num, end=" ")

# Задание 7:

def load_data(n):
     for i in range(1, n + 1):
          yield f"Получены данные {i}"

gen = load_data(5)
for data in gen:
     print(data)