# Задание 1:

numbers = [3, 5, 2, -1, 7]
print(all(n > 0 for n in numbers))

# Задание 2:

words = ["привет", "", "мир", "python"]
print(any(w == "" for w in words))

# Задание 3:

flags = [True, True, True, False]
print(all(flags))
print(any(flags))

# Задание 4:

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']

def check_win(f):
    return f == "x"

row_1 = all(map(check_win, field[:3]))
print(row_1)

# Задание 5:

P = ['0', '0', '0', '*', '0']
print(any("*" in p for p in P))

