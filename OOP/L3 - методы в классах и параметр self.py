# Задание 1:

class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

p1 = Person()
p2 = Person()
p1.set_data("Иван", 25)
p2.set_data("Александр", 30)

print(p1.get_data())
print(p2.get_data())

# Задание 2:

class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()

p.set_coords(7, 12) # set_coords - метод
print(p.get_coords()) # get_coords - метод

p.set_coords(-3, 5)
print(p.get_coords())

# Задание 3:

res = getattr(p, 'get_coords')
print(res)
print(res()) # (-3, 5)

print(p.get_coords()) # (-3, 5)