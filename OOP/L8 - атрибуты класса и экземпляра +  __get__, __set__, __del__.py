# Задание 1:

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return object.__getattribute__(self, '_SecureData__secret')

    def __getattribute__(self, item):
        if item == "_SecureData__secret":
            raise ValueError("Private attribute")
        return object.__getattribute__(self, item)

data = SecureData("пароль123")
# print(data.__secret) # ошибка
print(data.get_secret()) # "пароль123"

# Задание 2:

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def get_secret(self):
        return object.__getattribute__(self, '_SecureData__secret')

    def __getattribute__(self, item):
        if item == "_SecureData__secret":
            raise ValueError("Private attribute")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "token":
            raise AttributeError ("Нельзя создавать атрибут token")
        return object.__setattr__(self, key, value)

data = SecureData("123")
# data.token = "abc123" # ❌ AttributeError
data.other = "ok" # ✅ работает
print(data.get_secret())
print(data.other)

# Задание 3:

class SafeDict:

    def __getattr__(self, item):
        return "N/A"

    def __delattr__(self, item):
        print(f"Удалён атрибут {item}")
        return object.__delattr__(self, item)

d = SafeDict()
print(d.unknown) # "N/A"
d.key = 10
del d.key # "Удалён атрибут key"