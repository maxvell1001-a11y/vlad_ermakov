# Задание 1:

# age: int = 25
# name: str = 'John'
# height: float = 1.8
# is_online: bool = True

# print(age, name, height, is_online)

# Задание 2:

# def greet(name: str) -> str:
#     return f"Привет, {name}!"
#
# print(greet("Анна"))

# Задание 3:

# def multiply(a: int | float, b: int | float) -> int | float:
#     return a * b
#
# print(multiply(5, 4))

# Задание 4:
# from typing import Optional
#
# def describe_temperature(value: float, unit: Optional[str] = None) -> None:
#     if unit:
#         print(f"Температура: {value} {unit}")
#     else:
#         print(f"Температура: {value}")
#
# describe_temperature(36.6, "°C")
# describe_temperature(36.6)

# Задание 5:

# from typing import Final
#
# PI: Final = 3.14
# PI = 3.14159 # Предупреждение

# Задание 6:

# def area(length: float, width: float) -> float:
#     return length * width
#
# print(area.__annotations__)

# Задание 7:

Number = int | float

def square(x: Number) -> Number:
    return x ** 2

print(square(5))