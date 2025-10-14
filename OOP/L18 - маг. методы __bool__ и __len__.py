# Задание 1: Проверка "пустой точки"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y

p1 = Point(0, 0)
p2 = Point(2, 0)
assert not bool(p1) # False при координатах (0, 0), но из-за not будет True
assert bool(p2) # True при координатах (2, 0)

# Задание 2: Объект с __len__ вместо __bool__

class TextBlock:
    def __init__(self, content):
        self.content = content

    def __len__(self):
        return len(self.content)

txt = TextBlock("hello")
empty = TextBlock("")
assert bool(txt)
assert not bool(empty)

# Задание 3: Использование объекта в if

class ServerResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def __bool__(self):
        return self.status_code == 200

r = ServerResponse(200)
if r:
    print("✅")
else:
    print("❌")

r = ServerResponse(500)
assert not r
r2 = ServerResponse(200)
assert r2