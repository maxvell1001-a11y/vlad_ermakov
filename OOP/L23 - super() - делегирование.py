# Задания: super() и делегирование

class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label) # 100 200 OK

# Задание 2: Что будет без super?

class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

print(btn.__dict__) # {'x': 100, 'y': 200, 'label': 'OK'}

# Задание 3: Переопределение метода

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")

class HTMLLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print(f"<p>{msg}</p>")

logger = HTMLLogger()
logger.log("Login successful")