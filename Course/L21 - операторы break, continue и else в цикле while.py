# numbers = [1, 5, 3, 0, 1, 0, 2]
# found_even = False
# i = 0
#
# while i < len(numbers):
#     if numbers[i] % 2 == 0 and numbers[i] != 0:
#         print("Чётное число найдено:", numbers[i])
#         found_even = True
#         break
#     i += 1
# else:
#     print("Нет чётных чисел")

# s = 0
# num = 1
#
# while num != 0:
#     num = int(input("Введите число (0 для выхода): "))
#     if num < 0:
#         continue
#     s += num
#     print("Сумма положительных чисел:", s)
# print("Конец программы (вы ввели 0)")

# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
#
# if a > b:
#     a, b = b, a
#
# while a <= b:
#     if a % 2 == 0:
#         a += 1
#         continue
#     print(a)
#     a += 1

# N = int(input('Введите число N: '))
#
# if N < 2:
#     print("Число должно быть больше 1")
# else:
#     i = 2
#     while i < N:
#         if N % i == 0:
#             print("Число не является простым")
#             break
#         i += 1
#     else:
#         print("Число простое")

max_num = None

while True:
    num = input("Введите число (Enter или 0 для выхода): ")

    if num == "" or num == "0":
        break
    num = int(num)

    if max_num is None or num > max_num:
        max_num = num

print("Максимальное число:", max_num if max_num is not None else "Числа не введены")