# Задание 1: Использование стандартного менеджера контекста

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(file.read())
except Exception as e:
    print(f"Ошибка чтения файла: {e}")

# Задание 2: Свой менеджер для списка

class BackupList:
    def __init__(self, lst):
        self.lst = lst

    def __enter__(self):
        self.backup = self.lst[:]
        return self.lst

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.lst[:] = self.backup
        return False

data = [1, 2, 3]

try:
    with BackupList(data) as d:
        d[0] = 100
except:
    pass

print(data) # ✅ изменения сохранены только без ошибок

# Задание 3: Ловушка ошибок в менеджере

# def __exit__(self, exc_type, exc_val, exc_tb):
#     if exc_type is None:
#         self.lst[:] = self.backup
#     return True # ❗ Ошибки подавляются

# Задание 4: Вложенные менеджеры контекста

try:
    with open ("myfile.txt",) as fin:
        with open ("output.txt", "w") as fout:
            for line in fin:
                fout.write(line)
except Exception as e:
    print(f"Ошибка копирования: {e}")

# Задание 5: Менеджер для временных файлов

import os
from tempfile import TemporaryDirectory

with TemporaryDirectory() as tmpdir:
    filepath = os.path.join(tmpdir, "temp.txt")
    with open(filepath, "w") as f:
        f.write("Hello")

# Здесь временный каталог автоматически удалён