# Задание 1:

def multiply(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) * n
            return res
        return wrapper
    return decorator

@multiply(3)
def add(a, b):
    return a + b

print(add(2, 3))

# Задание 2:

def power(exp):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) ** exp
            return res
        return wrapper
    return decorator

@power(2)
def square_root(x):
    return x ** 0.5

print(square_root(16))  # (16 ** 0.5) ** 2 = 16

# Задание 3:

# def logger(log_file):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             with open(log_file, "a") as f:
#                 f.write(f"Функция {func.__name__}({args}, {kwargs}) = {result}\n")
#             return result
#         return wrapper
#     return decorator
#
# @logger("log.txt")
# def add(a, b):
#     return a + b
#
# add(2, 3)  # Записывает в log.txt

# Задание 4:

import time

def timer(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            for _ in range(repeat):
                start_time = time.time()
                func(*args, **kwargs)
                total_time += time.time() - start_time
            avg_time = total_time / repeat
            print(f"Среднее время выполнения: {avg_time:.4f} сек")
        return wrapper
    return decorator

@timer(3)
def slow_function():
    time.sleep(1)

slow_function()

# Задание 5:

from collections import OrderedDict


def cache(max_size):
    memory = OrderedDict()  # Используем OrderedDict для FIFO-удаления

    def decorator(func):
        def wrapper(*args):
            if args in memory:
                return memory[args]  # Возвращаем результат из кэша

            result = func(*args)  # Вычисляем результат
            memory[args] = result  # Сохраняем в кэше

            if len(memory) > max_size:
                memory.popitem(last=False)  # Удаляем самый старый элемент

            return result

        return wrapper

    return decorator


@cache(2)
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b


print(slow_add(2, 3))  # Вычисляет и кэширует
print(slow_add(2, 3))  # Берет из кэша
print(slow_add(4, 5))  # Вычисляет и кэширует
print(slow_add(2, 3))  # Старый результат удален, вычисляет заново