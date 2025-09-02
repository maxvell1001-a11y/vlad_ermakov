# a = [(i, j) for i in range(1, 4) for j in range(1, 5)]
# print(a)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# a = [[x ** 2 for x in row] for row in matrix]
# print(a)

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
#
# a = [x for row in matrix for x in row]
# print(a)

# M = int(input("Введите M: "))
# N = int(input("Введите N: "))
#
# matrix = [[i * M + j + 1 for j in range(M)] for i in range(N)]
# print(matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)