# Задание 1:

class Logger:
    __instance = None
    __is_init = False

    def __new__(cls, *args, **kwargs):
        print('Создание логгера')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not Logger.__is_init:
            print("Инициализация логгера")
        Logger.__is_init = True

    def log(self, message):
        pass

a = Logger()
b = Logger()

# Задание 2:

class Logger:
    __instance = None
    __is_init = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not Logger.__is_init:
            self.logs = []
            Logger.__is_init = True

    def log(self, message):
        self.logs.append(message)

a = Logger()
a.log("Первое сообщение")

b = Logger()
b.log("Второе сообщение")

print(a.logs) # ['Первое сообщение', 'Второе сообщение']
print(b.logs) # ['Первое сообщение', 'Второе сообщение']

# Задание 3:

class Logger:
    __instance = None
    __is_init = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not Logger.__is_init:
            self.logs = []
            Logger.__is_init = True

    def log(self, message):
        self.logs.append(message)

    def __del__(self):
        Logger.__instance = None
        Logger.__is_init = False
        print("Логгер удалён")

a = Logger()
a.log("Test")
del a

b = Logger()
b.log("New log")
print(b.logs)  # ['New log']