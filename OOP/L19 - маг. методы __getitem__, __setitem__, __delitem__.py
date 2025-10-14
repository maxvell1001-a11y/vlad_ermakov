# Задание 1: Индексация по предметам

class Diary:
    def __init__(self, grades=None):
        self.grades = grades or {}

    def __getitem__(self, key):
        if key in self.grades:
            return self.grades[key]
        else:
            raise KeyError("Предмет не найден")

d = Diary({'math': [5, 4], 'bio': [3, 4, 5]})
print(d["math"])
assert d['math'] == [5, 4]

# Задание 2: Добавление оценки по предмету | Задание 3: Удаление предмета

class Diary:
    def __init__(self, grades=None):
        self.grades = grades or {}

    def __getitem__(self, key):
        if key in self.grades:
            return self.grades[key]
        else:
            raise KeyError("Предмет не найден")

    def __setitem__(self, key, value):
        if isinstance (value, list):
            self.grades[key] = value
        elif isinstance (value, int | float):
            if key not in self.grades:
                self.grades[key] = []
            self.grades[key].append(value)
        else:
            raise TypeError("Оценка должна быть числом или списком")

    def __delitem__(self, key):
        if key not in self.grades:
            raise KeyError("Предмет не найден")
        else:
            del self.grades[key]

d = Diary({'math': [5, 4], 'bio': [3, 4, 5]})
d['math'] = 5 # добавляет 5
d['bio'] = [5, 5, 5] # заменяет список
print(d.grades) #{'math': [5, 4, 5], 'bio': [5, 5, 5]}

del d['bio']
print(d.grades) #{'math': [5, 4, 5]}