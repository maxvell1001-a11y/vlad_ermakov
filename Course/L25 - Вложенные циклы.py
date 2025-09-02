# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i * j:2}", end=" ")
#     print()

# matrix = [[1, 2, 17, 4],
#           [2, 31, 4, 5],
#         [3, 10, 5, 54]]
#
# max_value = matrix[0][0]
#
# for row in matrix:
#     for num in row:
#         if num > max_value:
#             max_value = num
#
# print("Матрица:")
# for row in matrix:
#     print(row)
#
# print(f"Максимальное число: {max_value}")

# matrix = [
#     [3, -2, 7, -9],
#     [-1, 6, -5, 4],
#     [8, -7, 3, -2]]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] < 0:
#             matrix[i][j] = 0  # Заменяем отрицательное число на 0
#
# print("Обновленная матрица:")
# for row in matrix:
#     print(row)

# board = []
#
# for i in range(8):
#     row = []
#     for j in range(8):
#         row.append((i + j) % 2)
#     board.append(row)
#
# for row in board:
#     print(row)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

for row in matrix:
    row.reverse()
    print(row)