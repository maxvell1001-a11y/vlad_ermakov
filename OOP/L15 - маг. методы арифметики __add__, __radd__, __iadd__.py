# Задание 1: Сумма времени

class Timer:
    def __init__(self, seconds):
        self.seconds = seconds % 86400

    def __add__(self, other):
        if isinstance(other, Timer):
            return Timer(self.seconds + other.seconds)
        elif isinstance(other, int):
            return Timer(self.seconds + other)
        raise TypeError("Можно складывать только Timer и int")

    def __radd__(self, other):
        return self + other

    def __str__(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

t1 = Timer(3600)
t2 = t1 + 125
t3 = 300 + t1
print(t2) # 01:02:05
print(t3) # 01:05:00

# Задание 2: Класс Score

class Score:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Score):
            return Score(self.value + other.value)
        elif isinstance(other, int):
            return Score(self.value + other)
        raise TypeError("Можно складывать только Score и int")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value += other
        elif isinstance(other, Score):
            self.value += other.value
        else:
            raise TypeError("Можно складывать только Score и int")
        return self

    def __str__(self):
        return f"Score: {self.value}"

s = Score(10)
s += 5

print(s) # Score: 15
print(s + 20) # Score: 35
print(100 + s) # Score: 115

# Задание 3: Сумма результатов тестов

class TestResult:
    def __init__(self, passed: int, failed: int):
        self.passed = passed
        self.failed = failed

    def __add__(self, other):
        if not isinstance(other, TestResult):
            raise TypeError("Можно складывать только TestResult")
        return TestResult(self.passed + other.passed, self.failed + other.failed)

    def __str__(self):
        return f"Passed: {self.passed} | Failed: {self.failed}"

t1 = TestResult(3, 1)
t2 = TestResult(2, 0)
t3 = t1 + t2
print(t3) # Passed: 5 | Failed: 1