# Задание 1:

counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(increment())
print(increment())
print(counter)

# Задание 2:

def local_variable():
    x = 10
    print(x)

local_variable()
# print(x) # Ошибка, х - локальная переменная

# Задание 3:

num = 5

def modify_global():
    global num
    num = 11
    print(num)

modify_global()
print(num) # c global num результат 11, без global num результат

# Задание 4:

def nested_func():
    x = 10

    def inner_func():
        nonlocal x
        x = 20
        print("inner:", x)

    inner_func()
    print("outer:", x)

nested_func()