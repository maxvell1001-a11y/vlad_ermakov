# Задание 1: Сравнение Clock

class Clock:
    __DAY = 86400
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть int")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Секунды должны быть int или Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc

c1 = Clock(3600)
c2 = Clock(7200)
assert c1 < c2
assert c1 == 3600
assert c2 != c1

# Задание 2: Сравнение пользователей

class User:
    def __init__(self, user_id , name):
        self.user_id = user_id
        self.name = name

    def __eq__(self, value):
        if isinstance(value, int):
            return self.user_id == value
        elif isinstance(value, User):
            return self.user_id == value.user_id
        raise TypeError("Неверный тип")

u1 = User(1, "Daniil")
u2 = User(1, "Ivan")
u3 = User(2, "Daniil")
assert u1 == u2
assert u1 != u3

# Задание 3: Класс

class Result:
    def __init__(self, passed: int, failed: int):
        self.passed = passed
        self.failed = failed

    def total(self):
        return self.passed + self.failed

    def rate(self):
        return self.passed / self.total()

    def __eq__(self, other):
        return self.total() == other.total()

    def __lt__(self, other):
        return self.rate() < other.rate()

    def __le__(self, other):
        return self.rate() <= other.rate()

    def __gt__(self, other):
        return self.rate() > other.rate()

    def __ge__(self, other):
        return self.rate() >= other.rate()

r1 = Result(8, 2) # 80%
r2 = Result(4, 1) # 80%
r3 = Result(9, 1) # 90%
assert r1 == r3
assert r3 > r2