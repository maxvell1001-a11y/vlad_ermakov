# N = int(input("Введите число: "))
#
# a = [x ** 2 for x in range(N) if x >= 1]
# print(a)

# a = [x for x in range(-10,11) if x % 2 == 0]
# print(a)

# N = input("Введите числа через пробел: ")
#
# a = [int(x) for x in N.split() if int(x) > 0]
# print(a)

# words = ["Python", "прост", "и", "мощен"]
#
# a = [len(w) for w in words]
# print(a)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]

a = ["четное" if x % 2 == 0 else "нечетное" for x in list]
print(a)