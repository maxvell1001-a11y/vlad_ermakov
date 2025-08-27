num = int(input("Введите число: "))
res = "Чётное" if num % 2 == 0 else "Нечётное"
print(res)

a = int(input("Первое число: "))
b = int(input("Второе число: "))
res = a if a > b else b
print(res)

num = int(input("Введите число: "))
res = "Отриц" if num < 0 else ("Зеро" if num == 0 else "Полож")
print(res)

num = int(input("Ваш возраст: "))
res = "Вам ещё рано" if num < 18 else "Уже можно"
print(res)

count = float(input("Сумма покупки: "))
final_price = count * 0.9 if count > 5000 else count
print("Итоговая сумма:", final_price)