# Задание 1:

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return "hello, world!"

print(say_hello())  # "HELLO, WORLD!"

# Задание 2:

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

# Задание 3:

def validate_args(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            raise ValueError("Аргументы должны быть положительными!")
        return func(*args, **kwargs)
    return wrapper

@validate_args
def add(a, b):
    return a + b

print(add(5, 10))  # 15
# print(add(-1, 10))  # ValueError: Аргументы должны быть положительными!

# Задание 4:

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

print(slow_add(2, 3))  # "Вычисляю 2 + 3..." 5
print(slow_add(2, 3))  # 5 (результат взят из кэша)

# Задание 5:

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e}")
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Ошибка: деление на ноль!