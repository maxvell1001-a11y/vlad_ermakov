# Задание 1: Порядок вызова __init__()

class A:
    def __init__(self):
        print("A.__init__()")
        super().__init__()

class B:
    def __init__(self):
        print("B.__init__()")
        super().__init__()

class C:
    def __init__(self):
        print("C.__init__()")
        super().__init__()

class D(A, B, C):
    def __init__(self):
        print("init D")
        super().__init__()

d = D()
print(D.__mro__)

# Задание 2: Проблема без super()

class Goods:
    def __init__(self):
        print("init Goods")
        super().__init__()

class MixinLog:
    def __init__(self):
        print("init MixinLog")

class NoteBook(Goods, MixinLog):
    pass

n = NoteBook()

# Задание 3: Конфликт методов

class Goods:
    def __init__(self):
        print("init Goods")
        super().__init__()

    def print_info(self):
        print("print_info() Goods")

class MixinLog:
    def __init__(self):
        print("init MixinLog")

    def print_info(self):
        print("print_info() MixinLog")

class NoteBook(Goods, MixinLog):
    pass

n = NoteBook()
n.print_info() # вызовет метод print_info() из класса Goods

# А если бы мы написали так:
#
# class NoteBook(MixinLog, Goods):
#     pass

# n.print_info() # вызовет метод print_info() из класса MixinLog