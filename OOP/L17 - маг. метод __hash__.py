# Задание 1: Хэшируемая точка

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 3)
assert p1 == p2
assert hash(p1) == hash(p2)
assert p1 != p3

# Задание 2: Использование в set

s = {Point(1, 2), Point(3, 4), Point(1, 2)}
print(len(s)) # 2

# Работает, потому что Point(1, 2) считается дубликатом благодаря __eq__ + __hash__

# Задание 3: Ключи-объекты в словаре

p = Point(5, 5)
d = {p: "центр"}
assert d[Point(5, 5)] == "центр"

# Без __hash__ будет TypeError
# Без __eq__ — создастся новый ключ, и d[Point(5, 5)] не найдётся

