# Задание 1:

class User:

    def set_credentials(self, login, password):
        if type(login) == str and type(password) == str:
            self.__login = login
            self.__password = password

    def get_credentials(self):
        return self.__login, self.__password

lp = User()
lp.set_credentials('admin', '<PASSWORD>')
print(lp.get_credentials())

lp.login = 'admin2'
print(lp.get_credentials()) # не меняется, т.к. login - приватный атрибут

# Задание 2:

class User:

    def set_credentials(self, login, password):
        if type(login) == str and type(password) == str:
            self.__login = login
            self.__password = password
        self.__encrypt_password(password)

    def get_credentials(self):
        return self.__login, self.__password

    def check_password(self, password):
        return self.__password == password

    def __encrypt_password(self, password):
        return self.__password.upper()

u = User()
u.set_credentials("daniil", "qwerty")

print(u.check_password("qwerty")) # True
print(u.check_password("qwe")) # False

# Задание 3:

# print(u.__encrypt_password("qwerty")) # нельзя вызвать, потому что атрибут приватный
# print(u.__password) # нельзя вызвать, потому что атрибут приватный

print(u._User__password) # можно вызвать, но это плохая практика - нарушение инкапсуляции
print(u._User__encrypt_password("x")) # можно вызвать, но это плохая практика - нарушение инкапсуляции