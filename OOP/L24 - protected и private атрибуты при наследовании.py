# Задание 1: Ошибка с private-атрибутом

class Widget:
    __name = 'Widget'

    def __log(self):
        pass

class Button(Widget):
    pass

b = Button()
# print(b.__name) # Ошибка: атрибут __name private
# print(b.__log()) # Ошибка: атрибут __log private

# Задание 2: Правильная реализация через protected

class Widget:
    def __init__(self, name):
        self._name = name

    def _log(self):
        print(f"[LOG]: {self._name}")

class Button(Widget):

    def print_name(self):
        print(self._name)
        self._log()

btn = Button("OK")
print(btn._name)
btn._log()

# Задание 3: Проверка имени в __dict__

btn = Button("OK")

print(btn.__dict__)
print(dir(btn))