# N = int(input("Введите число: "))
# i = 1
#
# while i <= N:
#     print(i)
#     i += 1

# N  = int(input("Введите число: "))
# i = 2
# s = 0
#
# while i < N:
#     s += i
#     i += 2
# print("Сумма чётных чисел: ", s)

# N = int(input("Введите натуральное число: "))
# s = 0
#
# while N > 0:
#     s += 1
#     N //= 10
# print("Количество цифр:", s)

# num = int(input("Введите натуральное число: "))
# max_digit = 0

# while num > 0:
#     last_digit = num % 10  # Получаем последнюю цифру
#     if last_digit > max_digit:
#         max_digit = last_digit  # Обновляем максимум
#     num //= 10  # Убираем последнюю цифру
#
# print("Максимальная цифра числа:", max_digit)

correct_password = "qwerty123"
ps = ""

while ps != correct_password:
    ps = input("Введите пароль: ")

print("Вход в систему осуществлен")