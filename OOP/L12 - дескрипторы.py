# Задание 1:

class StringField:
    @classmethod
    def verify(cls, value):
        if type(value) != str or value == "":
            raise TypeError("Данные должны быть строкой")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

class User:

    name = StringField()
    surname = StringField()

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

u = User("Daniil", "Petrov")
# u.name = "" # ❌ ValueError
# u.surname = 123 # ❌ TypeError

# Задание 2:

class RangeIntegerField:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Значение должно быть целым числом")
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Число должно быть в диапазоне [{self.min_value}, {self.max_value}]")
        setattr(instance, self.name, value)

class Product:
    count = RangeIntegerField(0, 1000)

    def __init__(self, count):
        self.count = count

p = Product(10)
# p.count = 1200 # ❌ ValueError
# p.count = "100" # ❌ TypeError

# Задание 3:

class BooleanField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) is not bool:
            raise TypeError("Значение должно быть True или False")
        setattr(instance, self.name, value)

class FeatureToggle:
    is_active = BooleanField()

    def __init__(self, flag):
        self.is_active = flag

f = FeatureToggle(True)
f.is_active = False
# f.is_active = "yes" # ❌ TypeError