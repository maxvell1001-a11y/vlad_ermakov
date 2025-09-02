# N = int(input("Введите высоту треугольника: "))
#
# for i in range(1, N):
#     print('*' * i)

# N = int(input("Введите число: "))
# s = 0
#
# if N < 1:
#     print("Число должно начинаться с 1")
# else:
#     for i in range(1, N, 2):
#         s += i + 1
# print(f"Сумма чётных чисел от 1 до {N}: {s}")

nums = [4, 3, -10, 23, -5, 8, 11]
found = False

for i in nums:
    if i < 0:
        print(f"В списке есть отрицательное число: {i}")
        found = True
        break

if not found:
    print("В списке нет отрицательных чисел.")