cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [17, "хей хай", True, 5.6]
print(cities[0])
print(numbers[-1])
#print(cities[10])
numbers = [1, 10, 3, 4, 5]
mixed = [17, "хей хай", True, "Python"]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print([1, 2, 3] + [4, 5])
P = ["Python", "is", "awesome"]
print(P * 3)
print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)
del numbers[2]  # Удаляем третий элемент
print(numbers)  # [1, 10, 4, 5]
del cities[-1]
print(cities)
print(list("Python"))  # ['P', 'y', 't', 'h', 'o', 'n']
print(list(min("Python")))
print(list(max("Python")))