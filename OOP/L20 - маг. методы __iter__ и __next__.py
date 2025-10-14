# Задание 1: Итерируемый список ошибок

class ErrorList:
    def __init__(self, errors: list):
        self.errors = errors

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.errors):
            raise StopIteration

        res = self.errors[self._index]
        self._index += 1
        return res

errs = ErrorList(["Ошибка 1", "Ошибка 2"])

for msg in errs:
    print(msg)

# Задание 2: Итератор логов с фильтрацией

class LogLines:
    def __init__(self, lines, keyword):
        self.lines = lines
        self.keyword = keyword

    def __iter__(self):
        self.filtered = [line for line in self.lines if self.keyword in line]
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.filtered):
            raise StopIteration

        line = self.filtered[self._index]
        self._index += 1
        return line

logs = LogLines(["ok", "error: not found", "error: timeout", "success"], "error")

for line in logs:
    print(line)  # выведет две строки с "error"

# Задание 3: Итерируемая фикстура

class TestUserGenerator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= self.count:
            raise StopIteration

        self._current += 1
        return f"User_{self._current}"

gen = TestUserGenerator(3)
for user in gen:
    print(user)