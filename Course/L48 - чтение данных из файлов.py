# Задание 1:

file = open("data.txt", encoding="utf-8")
# print(file.read())

# Задание 2:

# print(file.readline())

# Задание 3:

# print(file.readline(10))

# Задание 4:

# lst = file.readlines()
#
# print(lst)

# Задание 5:

# for line in file:
#     print(line, end="")

# Задание 6:

# print(file.read(6))
# file.seek(0)
# print(file.read(6))

# Задание 7:

# file.seek(0, 2)
# print(f"Размер файла: {file.tell()} байт")

# Закрываем файл
file.close()

# Задание 8:

with open("data.txt", encoding="utf-8") as file:
    print(file.read())
