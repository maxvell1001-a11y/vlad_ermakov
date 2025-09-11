# Задание 1:

def summarize(*args):
    return sum(x for x in args if isinstance(x, (int, float)))

print(summarize(1, 2, 3))
print(summarize(10, "abc", 5, 2))

# Задание 2:

def format_text(*words, sep=" ", uppercase=False):
    text = sep.join(words)
    return text.upper() if uppercase else text

print(format_text("Hello", "world", "!"))
print(format_text("python", "rocks", sep="-"))
print(format_text("make", "it", "LOUD", uppercase=True))

# Задание 3:

def create_profile(name, age, **extra):
    print("Профиль пользователя:")
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    if extra:
        print("Дополнительная информация:")
        for key, value in extra.items():
            print(f"  {key}: {value}")

create_profile("Иван", 30, city="Москва", job="Инженер")

# Задание 4:

def generate_path(disk, *folders, filename, ext="txt", sep="\\"):
    path = sep.join((disk, *folders, f"{filename}.{ext}"))
    return path

print(generate_path("C:", "Users", "Admin", filename="document"))
print(generate_path("D:", "Projects", filename="app", ext="py"))
print(generate_path("F:", "Music", "Rock", filename="song", ext="mp3", sep="/"))

# Задание 5:

def process_orders(*orders, discount=0):
    total = sum(orders)
    discounted_total = total * (1 - discount / 100)
    print(f"Сумма заказа: {total}")
    print(f"С учетом скидки: {discounted_total}")

print(process_orders(100, 200, 300, discount=10))