# Задание 1:

class Cat:
    def __init__ (self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} говорит: мяу!")


cat = Cat("Мейн-кун", "Лео", 2)
cat.meow() # Лео говорит: мяу!