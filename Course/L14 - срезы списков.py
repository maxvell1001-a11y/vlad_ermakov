cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург"]
d = cities[:]
print(d)
print(id(cities), id(d))
print(cities[1:3])
print(cities[2:])
print(cities[:3])
print(cities[:])
print(cities[-2:])
print(cities[1::2])
print(cities[::-1])
print(cities[-2::-2])
cities[1:3] = ["Сочи", "Нижний Новгород"]
print(cities)
cities[::-2] = ["Город", "Город"]
print(cities)
cities[1:3] = ["Волгоград", "Омск"]
print(cities)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
c = ["Python", "rocks"]
print(c *2 )
print([1, 2, 3] == [1, 2, 3])
print([10, 5, 3] > [5, 10, 3])
chars = list("Python")
print(max(chars), min(chars))
print(sum(chars)) # Ошибка