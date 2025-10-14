# Задание 1: Валидатор длины строки

# В Python валидатор — это функция, класс или вызываемый объект,
# который проверяет, соответствует ли значение определённым правилам или формату.
# Если значение корректно, валидатор может вернуть его (возможно, изменённое),
# а если нет — вызвать ошибку ValidationError. Это позволяет гарантировать
# целостность и надежность данных в приложениях.


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValueError(f"Длина должна быть не менее {self.min_length} символов")
        elif len(value) > self.max_length:
            raise ValueError(f"Длина должна быть не более {self.max_length} символов")
        else:
            return value

validator = LengthValidator(3, 10)
print(validator("python")) # ✅ True
# print(validator("hi")) # ❌ ValueError

# Задание 2: Множественный вызов с накоплением

class Sumator:
    def __init__(self):
        self.total = 0

    def __call__(self, value):
        if value:
            self.total += value
        return self.total

s = Sumator()
print(s(5)) # 5
print(s(10)) # 15
print(s(-2)) # 13

# Задание 3: Функтор для автотестов

class HasText:
    def __init__(self, text):
        self.text = text

    def __call__(self, value):
        return self.text in value


assert HasText("Success")("Test passed: Success")  # ✅ True
# assert HasText("Error")("All OK")  # ❌ False