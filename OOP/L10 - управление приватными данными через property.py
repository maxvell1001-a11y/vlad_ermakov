# Задание 1:

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Зарплата должна быть положительной")

    @salary.deleter
    def salary(self):
        del self.__salary
        print("Зарплата удалена")

e = Employee("Daniil", 5000)
print(e.salary) # 5000

e.salary = 8000
print(e.salary) # 8000
# e.salary = -100 # ❌ ValueError

# Задание 2:

del e.salary
print(e.__dict__) # salary нет

# Задание 3 (на автотесты):

class LoginForm:
    def __init__(self):
        self.__username = ""

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        print("username изменён")
        self.__username = value


form = LoginForm()

form.username = "admin" # выводит лог "username изменён"
print(form.username) # "admin"