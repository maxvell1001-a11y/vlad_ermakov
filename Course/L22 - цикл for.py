# a = input('Напишите символы: ')
#
# for i in a[::-1]:
#     print(i, end="")

# s = [1, 3, 5, -1, 19, 2, 4]
#
# for i in range(len(s)):
#     if s[i] % 2 == 0:
#         s[i] = 0
# print(s)

# N = int(input("Введите число N: "))
# a = []
#
# for i in range(N + 1):
#     a.append(2 ** i)
#
# print(a)

# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# K = int(input("Введите число K: "))
#
# for i in range(A, B + 1, K):
#     print(i, end=" ")

N = int(input("Введите число N: "))
S = 0

for i in range(2, N + 1):
    S += 1 / i

print(S)