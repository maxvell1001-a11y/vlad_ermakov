# Задание 1

a = (True, [1, 2, 3], "hello", 5, {"key": "value"})

print(a[1], a[-1])

# Задание 2

nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)

print(nums.count(4))
print(nums.index(7))

# Задание 3

lst = ["Python", "Java", "C++", "JavaScript"]

tup = tuple(lst)
print(tup)
print("C++" in tup)

# Задание 4

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup[:3])
print(tup[-3:])
print(tup[::2])

# Задание 5

b = ([1, 2, 3], {"ночь": "night"})

b[0].append(4)
b[1].setdefault("день", "day")
print(b)