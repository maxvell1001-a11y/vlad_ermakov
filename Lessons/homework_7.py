# num = 1000
# sum_2 = 0
# i  = 1
#
# while i <= num:
#     i += 1
#     sum_2 += i
#
# print(sum_2)
#
# input_password = input("Введите пароль: ")
# correct_password = "Пароль123"
# counter = 1
#
# while input_password != correct_password:
#     print(f"Пароль введен неправильно. Попытка {counter} из 3")
#     input_password = input("Введите пароль: ")
#     counter += 1
#     if counter == 3:
#         print("Вы ввели пароль 3 раза неправильно")
#         break
#
# print("Пароль верен")
#
# numbers = [23, 43, 75, 33, 80, 51, 62]
# result = []
# i = 0
#
# while True:
#     if numbers[i] % 2 == 0:
#         result.append(numbers[i])
#     i += 1
#     if i == len(numbers):
#         break
#
# print(result)
#
# num = 1
# res_sum = 0
#
# while num != 0:
#     imput_num = input("Введите целое число или 0 для выхода: ")
#     if not imput_num.isdigit():
#         print("Введено не число")
#         break
#     num = int(input("Введите целое число или 0 для выхода: "))
#
#
#     if num % 2 == 0:
#         continue
#     res_sum += num
# else:
#     print("Сумма целых нечётных чисел:", res_sum)

# 1. Вывод чисел от 1 до N

# N = int(input("Введите целое число: "))
# i = 1
#
# while i <= N:
#     print(i, end=" ")
#     i += 1

# 2. Сумма четных чисел до N

# N = int(input("Введите целое число: "))
# s = 0
# i = 1
#
# while i <= N:
#     if i % 2 == 0:
#         s += i
#     i += 1
#
# print("Сумма чётных чисел до", N, ":", s)

# 3. Подсчет количества цифр в числе

# N = int(input("Введите натуральное число: "))
# s = 0
#
# while N > 0:
#     s += 1
#     N //= 10
# print("Количество цифр:", s)

# 4. Определение максимальной цифры в числе

# N = int(input("Введите натуральное число: "))
# max_digit = 0
#
# while N > 0:
#     last_digit = N % 10  # Получаем последнюю цифру
#     if last_digit > max_digit:
#         max_digit = last_digit  # Обновляем максимум
#     N //= 10  # Убираем последнюю цифру
#
# print("Максимальная цифра числа:", max_digit)

# 5. Запрос пароля

# password = input("Введите пароль: ")
# good_password = "1qwerty123"
#
# while password != good_password:
#     print("Пароль введен неправильно")
#     password = input("Введите пароль: ")
# print("Пароль верен")

# 1. Поиск первого четного числа

# numbers = [1, 5, 3, 0, 1, 0, 2]
# i = 0
#
# while i < len(numbers):
#     if numbers[i] % 2 == 0 and numbers[i] != 0:
#         print("Первое четное число:", numbers[i])
#         break
#     else:
#         i += 1
# else:
#     print("Четное число не найдено")

# 2. Пропуск отрицательных чисел

# N = 1
# s = 0
#
# while N != 0:
#     N = int(input("Введите положительное число, 0 для выхода: "))
#     if N < 0:
#         continue
#     s += N
# print("Сумма положительных чисел:", s)

# 3. Вывод нечетных чисел из диапазона

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите начало диапазона: "))
#
# if a > b:
#     a, b = b, a
#
# while a <= b:
#     if a % 2 == 0:
#         a += 1
#         continue
#     print(a, end=" ")
#     a += 1

# 4. Проверка на простое число

# N = int(input("Введите число N: "))
#
# if N < 2:
#     print("Число должно быть больше 1")
# else:
#     i = 2
#     while i < N:
#         if N % i == 0:
#             print("Число не простое")
#             break
#         i += 1
#     else:
#         print("Число простое")

# 5. Поиск максимального числа

# max_num = None
#
# while True:
#     num = input("Введите число (Enter или 0 для выхода): ")
#
#     if num == "" or num == "0":
#         break
#     num = int(num)
#
#     if max_num is None or num > max_num:
#         max_num = num
#
# print("Максимальное число:", max_num if max_num is not None else "Числа не введены")

# 1. Вывести все символы строки в обратном порядке

# N = input("Введите строку: ")
#
# for i in N[::-1]:
#     print(i, end="")

# 2.Замена четных элементов списка на 0

# N = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(0, len(N)):
#     if N[i] % 2 == 0:
#         N[i] = 0
# print(N)

# 3. Генерация списка степеней двойки

# N = int(input("Введите число: "))
# for i in range(N):
#     print(2 ** i, end=" | ")

# 4. Вывод всех чисел от A до B с шагом K

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
K = int(input("Введите число K: "))

if A > B:
    A, B = B, A

for i in range(A, B + 1, K):
    print(i, end=" ")