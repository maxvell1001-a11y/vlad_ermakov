# Задание 1:

lst = [10, 15, 22, 33, 40, 55, 60, 75, 80]

a = filter(lambda x: x % 2 == 0, lst)
print(list(a))

# Задание 2:

lst = ["apple", "123", "hello", "world42", "python3", "banana"]

a = filter(str.isalpha, lst)
print(list(a))

# Задание 3:

lst = [-5, 10, -2, 8, 0, -1, 15]

a = filter(lambda x: x > 0, lst)
print(list(a))

# Задание 4:

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = filter(is_prime, range(50))
print(list(a))

# Задание 5:

lst = ["Москва", "Архангельск", "Астрахань", "Казань", "Воронеж", "Анапа"]

a = filter(lambda city: city.startswith("А"), lst)
print(list(a))

# Задание 6:

lst = [15, 30, 45, 22, 60, 77, 90, 100]

a = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, lst))
print(a)

# Задание 7:

digit_lst = ["hello", "world42", "python3", "abc", "123", "data1science"]

a = list(filter(lambda word: any(char.isdigit() for char in word), digit_lst))
print(a)