# Задание 1:

numbers: list[int]  = [1, 2, 3]
names: list[str]  = ["John", "Jane"]
coords: tuple[float, float] = (1.0, 2.0)

print(numbers, names, coords)

# Задание 2:

grades: dict[str, int] = {"John": 90, "Jane": 85, "Bob": 95}
print(grades)

# Задание 3:

text = "python is fun and powerful"

unique_words: set[str] = set(text.split())
print(unique_words)

# Задание 4:

def get_upper(words: list[str]) -> list[str]:
    return list(map(lambda x: x.upper(), words))

print(get_upper(["привет", "мир"]))

# Задание 5:

def sum_positive(digits: list[int | float]) -> float:
    return sum(filter(lambda x: x > 0, digits))

print(sum_positive([5, -3.5, 2.2, 0, -1, 10]))

# Задание 6:

from typing import Callable

def filter_list(f: Callable[[int], bool], data: list[int]) -> list[int]:
    return list(filter(f, data))

print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))

# Задание 7:

def print_info(name: str, age: [int], tags: list[str]) -> None:
    print(name, age, tags)

# Задание 8:

from typing import Optional

def analyze(data: Optional[list[int]]) -> None:
    if data:
        print("Количество:", len(data))
        print("Среднее:", sum(data) / len(data))
    else:
        print("Список пуст или None")

analyze([10, 20, 30])
analyze(None)