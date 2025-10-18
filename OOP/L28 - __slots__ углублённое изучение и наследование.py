# Задание 1: Ошибка при добавлении нового поля

class UserDTO:
    __slots__ = ('id', 'email')

    def __init__(self):
        self.id = None
        self.email = None

u = UserDTO()
u.id = 1
u.email = 'user@example.com'
# u.username = 'admin' # ❌ Нельзя

# Задание 2: Экономия памяти

class A:
    def __init__(self):
        self.a = 1
        self.b = 2

class B:
    __slots__ = ('a', 'b')

    def __init__(self):
       self.a = 1
       self.b = 2

print(A().__sizeof__()) # 16
print(B().__sizeof__()) # 32 - Класс с __slots__ экономит память, потому что не создаёт __dict__

# Задание 3: Наследование без ограничения

class Base:
    __slots__ = ('x',)

class Sub(Base):
    pass

s = Sub()
s.x = 1
s.y = 2 # ✅ работает, потому что нет __slots__ в Sub

# Задание 4: Наследование с ограничением

class Base:
    __slots__ = ('x',)
class Sub(Base):
    __slots__ = ('y',)

s = Sub()
s.x = 1
s.y = 2
# s.z = 3 # ❌ ошибка

# Задание 5: Проверка __dict__

class A:
    def __init__(self):
        self.a = 1
        self.b = 2

class B:
    __slots__ = ('a', 'b')

    def __init__(self):
        self.a = 1
        self.b = 2

a = A()
b = B()
print(hasattr(a, '__dict__')) # ✅ True
print(hasattr(b, '__dict__')) # ❌ False

# Задание 6: @property и __slots__

class Point:
    __slots__ = ('x', 'y', '_length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._length = (x ** 2 + y ** 2) ** 0.5

    @property
    def length(self):
        return self._length


p = Point(3, 4)
print(p.length) # 5.0

# length не нужно указывать в __slots__ , потому что это property —
# атрибут класса, а не экземпляра