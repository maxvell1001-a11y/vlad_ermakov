# Задание 1:

class Config:
    __shared_attrs = { "debug": True, "version": "1.0"}

    def __init__(self):
        self.__dict__ = self.__shared_attrs

c1 = Config()
c2 = Config()

c1.debug = False
print(c2.debug) # False

# Задание 2:

class Config:
    __shared_attrs = { "debug": True, "version": "1.0"}

    def __init__(self):
        self.__dict__ = self.__shared_attrs

    def show(self):
        for key, value in self.__dict__.items():
            print(f"{key} = {value}")

c1 = Config()
c2 = Config()
c1.show()
print("---")
c2.show()

# Задание 3:

cfg1 = Config()
cfg2 = Config()

cfg1.user = "Daniil"
print(cfg2.user) # Daniil

cfg2.user = "Sergey"
print(cfg1.user) # Sergey