# def decor(func):
#     def wrapper(*args, **kwargs):
#         print("До выполнения функции")
#
#         print("args", args)
#         print("kwargs", kwargs)
#         func(*args, **kwargs)
#         print("После выполнения функции")
#     return wrapper
#
# @decor
# def print_text(text):
#     print(f"простой текст {text}")
#
# print_text(text="Дополнительный текст")
#
#
# import time
#
# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Время выполнения: {end_time - start_time} сек")
#         return result
#     return wrapper
#
# @count_time
# def func_1():
#     time.sleep(3)
#     print('Функция отработала')
#     return "Возврат из функции"
#
# res = (func_1())
# print(res)


# 1. Напишите декоратор uppercase_decorator,
# который делает результат выполнения функции прописными буквами.

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"
print(say_hello())

# 2. Создайте декоратор repeat(n), который выполняет функцию n раз.

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hello!")

hello()

# 3. Создайте декоратор cache, который кэширует результаты выполнения функции.
# Если функция вызывается с теми же аргументами –
# возвращать сохраненный результат вместо нового вычисления.

def cache(func):
    memory = {}  # Кэш результатов
    def wrapper(*args):
        if args in memory:
            return memory[args]  # Возвращаем закэшированное значение
        result = func(*args)
        memory[args] = result  # Сохраняем в кэше
        return result
    return wrapper

@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b

print(slow_add(2, 3))
print(slow_add(2, 3))

# 4. Создайте декоратор с таймером timer(repeat),
# который выполняет функцию repeat раз и выводит среднее время выполнения.

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