# 1. Оставь только строки и списки из списка:

items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]

print(list(filter(lambda x: isinstance(x, (str, list)), items)))

# 2. Создай функцию describe_type(x), которая:

def describe_type(x):
    if isinstance(x, str):
        print(f"Это строка")
    elif type(x) is bool:
        print(f"Это булево значение")
    elif isinstance(x, (int, float)):
        print("Это число")
    else:
        print(f"Неизвестный тип")

describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])

# 3. Создай функцию filter_list(f, data: list[int]) -> list[int]

def filter_list(f, data: list[int]) -> list[int]:
    return list(filter(f, data))

result = filter_list(lambda x: x > 3, [1, 3, 5, 7])
print(result)

# 4. Добавь аннотацию типов в следующую функцию и укажи, что она возвращает None:

def print_info(name: str, age: [int], tags: list[str]) -> None:
    print(name, age, tags)

# 5. Создай функцию def analyze(data)

def analyze(data: list[float | int]) -> None:
    if not data:
        print("Список пустой.")
        return
    count = len(data)
    average = sum(data) / count
    print(f"Количество элементов: {count}")
    print(f"Среднее значение: {average}")

analyze([1, 2, 3, 4, 5])
analyze([])

# 6. Список логических значений:

flags = [True, True, True, False]

print(all(flags))
print(any(flags))

# 7. Поле в игре "Крестики-нолики" представлено так:

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']

print(all(flags[:3]))

# 8. На поле для "Сапёра" находится мина, если в ячейке символ *. Есть ли мина?

P = ['0', '0', '0', '*', '0']

print(any(P))

# 9. Выбери случайное значение из списка:

import random

colors = ["red", "green", "blue", "yellow", "purple"]
print(random.choice(colors))

# 10. Сгенерируй 10 случайных чисел от 0 до 100 и выведи их. Сделай так, чтобы результат был одинаковый при каждом запуске.

random.seed(0)
print([random.randint(0, 100) for _ in range(10)])

# 11. Напиши функцию greet(), которая принимает строку name и возвращает строку Привет, <name>!.

def greet(name: str) -> str:
    return f"Привет, {name}!"

print(greet("Анна"))

# 12. Создай функцию multiply(a, b), которая принимает два числа int или float и возвращает их произведение.

def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

print(multiply(5, 4))

# 13. Проверь типы аргументов функции через __annotations__.

def area(length: float, width: float) -> float:
    pass

print(area.__annotations__)
