# Задание 1:

class User:
    def __init__(self, email):
        self.__email = email

    @classmethod
    def verify_email(cls, email):
        if "@" not in email or "." not in email:
            raise ValueError("Некорректный email")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.verify_email(value)
        self.__email = value

u = User("test@example.com")
print(u.email) # test@example.com
u.email = "admin@mail.ru"
# u.email = "wrong_email" # ❌ ValueError
print(u.email)

# Задание 2:

class User:
    def __init__(self, email, age):
        self.email = email
        self.age = age

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Некорректный email")
        self.__email = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if type(value) is not int or not (18 <= value <= 99):
            raise ValueError("Возраст должен быть от 18 до 99")
        self.__age = value

u = User("admin2@mail.ru", 18)
print(u.email)

# Задание 3 (автотестовый кейс):

class RequestBody:
    def __init__(self, username: str, password: str, active: bool) -> None:
        self.username = username
        self.password = password
        self.active = active

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if type(value) is not str:
            raise ValueError("Имя пользователя должно быть строкой")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if type(value) is not str or len(value) < 6:
            raise ValueError("Пароль должен быть строкой и длиной не менее 6 символов")
        self.__password = value

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        if type(value) is not bool:
            raise ValueError("Активность должна быть булевой")
        self.__active = value

req = RequestBody("tester", "qwerty123", True)
print(req.username) # tester
# req.password = "123" # ❌ ValueError
print(req.__dict__) # {'username': 'tester', 'password': 'qwerty123', 'active': True}