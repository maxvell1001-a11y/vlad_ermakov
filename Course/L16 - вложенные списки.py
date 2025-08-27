matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
print(matrix)
print(matrix[1])
print(matrix[2][0])
matrix[0] = [0, 0, 0, 0]
print(matrix)
matrix[2][-1] = "Python"
print(matrix)
print((matrix[2]) * 2)
t = [["Люблю", "тебя", "Петра", "творенье"],
     ["Люблю", "твой", "строгий", "стройный", "вид"],
     ["Невы", "державное", "теченье"],
     ["Береговой", "ее", "гранит"]]
print(t[0])
print(t[1][2])
t[0][0] = "Я"
print(t)
t = t + [["Vlad", "Pitonn"]]
print(t)
A = [[[True, False], [1, ['com', 'by'], 3]], ["матрица", "вектор"]]
print(A[0][1][1])
print(A[0][1][1][0])
chess_board = [["B" if (i + j) % 2 == 0 else "W" for j in range(8)] for i in range(8)]
print(chess_board)
chess_board[3][3] = "Q"
chess_board[3][4] = "Q"
chess_board[4][3] = "Q"
chess_board[4][4] = "Q"
print(chess_board)