# 1. Создание списков

cities = ["Москва", "Тверь", "Вологда"]
numbers = [1, 2, 3, 4, 5]
mixed = [12, "Москва", True, 3.14]

# 2. Доступ к элементам списка

print(cities[0])
print(numbers[-1])
# print(cities[10]) # Такого элемента нет в списке

# 3. Изменение элементов списка

numbers[1] = 10
print(numbers)

mixed[-1] = "Python"
print(mixed)

# 4. Функции для работы со списками

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# 5. Операции со списками

a = [1, 2, 3]
b = [4, 5]

res = a + b
print(res)
print(["Python", "is", "awesome"] * 3)

# 6. Проверка вхождения

print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)

# 7. Удаление элементов

del numbers[2]
del cities[-1]
print(numbers, cities, sep="\n")

# 8. Дополнительное задание

lst = list("Python")
print(lst)
print(min(lst), max(lst))
# print(sum(lst)) # Ошибка, так как не все элементы списка могут быть числами

# 1. Создание и копирование списков

cities = ["Москва", "Тверь", "Вологда", "Казань", "Санкт-Петербург"]

cities2 = cities[::]
cities3 = list(cities2)
print(id(cities), id(cities2), id(cities3))

# 2. Извлечение элементов с помощью срезов

print(cities[1:3])
print(cities[2:])
print(cities[:4])
print(cities[::])
print(cities[-2:])

# 3. Использование шагов в срезах

print(cities[::2])
print(cities[::-1])
print(cities[-2::-2])

# 4. Изменение элементов списка через срезы

cities[1:3] = ["Сочи", "Нижний Новгород"]
print(cities)
cities[1::2] = ["Город"] * len(cities[1::2])
print(cities)
cities[1:3] = "Волгоград", "Омск"
print(cities)

# 5. Операции с объединением списков

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(["Python", "rocks"] * 2)

# 6. Сравнение списков

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print([10, 5, 3] > [5, 10, 3])
print([1, 2, 3] != [1, 2, "abc"]) # Возможно только == и !=

# 7. Дополнительное задание

chars = list("Python")
print(max(chars), min(chars))
# print(sum(chars)) # Нельзя суммировать строки

# 1. Добавление элементов

num = [5, 10, 15]
num.append(20)
num.insert(1, 7)
num.append("Python")
print(num)

# 2. Удаление элементов

num.remove(10)
last_num = num.pop() # Удаляет последний элемент
print(num) # Выводит список без последнего элемента
print(last_num) # Выводит последний элемент
index_num = num.pop(1) # Удаляет элемент по индексу
print(num)
print(index_num)

num.clear() # Очищает список
print(num) # Выводит пустой список

# 3. Копирование списков

letters = ["a", "b", "c"]

letters2 = letters[:]
letters3 = list(letters)
letters4 = letters.copy()
print(id(letters), id(letters2), id(letters3), id(letters4))
print(letters == letters3)

# 4. Поиск элементов

marks = [2, 3, 5, 3, 4, 5, 2, 3]

print(marks.count(3)) # Количество элементов 3
print(marks.index(5)) # Индекс первого элемента 5
print(6 in marks) # Проверка вхождения элемента 6
# print(marks.index(6)) # Ошибка, так как элемента 6 нет в списке

# 5. Изменение порядка элементов

nums = [8, 2, 5, 1, 7]

nums.sort() # Сортировка по возрастанию
print(nums)
nums.sort(reverse=True) # Сортировка по убыванию
print(nums)
nums.reverse() # Обратный порядок
print(nums)

# 6. Сортировка строк

cities = ["Москва", "Тверь", "Вологда", "Казань", "Санкт-Петербург"]

cities.sort()
print(cities)
print(cities.sort()) # Выводит None, так как метод ничего не возвращает
print(sorted(cities))

# 7. Дополнительное задание

chars = list("programming")

print(chars.count("g"))
chars.reverse()
print(chars)
chars.sort()
print(chars) # Сортировка по алфавиту

# 1. Создание вложенного списка

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(a)
print(a[1])
print(a[2][0]) # Выводит первый элемент третьей строки

# 2. Изменение элементов вложенного списка

a[0] = [0, 0, 0]
print(a)
a[1][-1] = "Python"
print(a)