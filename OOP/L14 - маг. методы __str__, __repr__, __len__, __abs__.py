# Задание 1: Удобный вывод объекта

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.author} — {self.title}"

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

book = Book("1984", "Джордж Оруэлл")
print(book)
print(repr(book))

# Задание 2: Модель ответа с len() и abs()

class ApiResponse:
    def __init__(self, data: list, expected):
        self.data = data
        self.expected = expected

    def __len__(self):
        return len(self.data)

    def __abs__(self):
        return abs(len(self.data) - self.expected)

r = ApiResponse([1, 2, 3], expected=5)
print(len(r)) # 3
print(abs(r)) # 2

# Задание 3: Класс с автотестовым __repr__

class TestUser:
    def __init__(self, id , name , email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<TestUser id={self.id} name='{self.name}' email='{self.email}'>"

user = TestUser(12, "Daniil", "daniil@example.com")
print(user)