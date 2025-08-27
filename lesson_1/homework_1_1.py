from pstats import count_calls

name = "Владислав"
age = 29
height = 111.1
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)
x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
a = 10
b = a
print(a, b) # Изменил значние с 7 на 10, b не изменился, потому что b = a
x = y = z = 10
print(x, y, z)
print(id(x), id(y), id(z))
x, y , z = 1, 2, 3
print(id(x), id(y), id(z))
a = 5
b = 10
a, b = b, a
print(a, b)
import keyword
print(keyword.kwlist)
var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1), type(var2), type(var3))
A_str = "Hello"
count_F = 0
a_str = "Hello_2"
ооо_222 = "Hello_3"
ффф_222 = "Hello_4"
print(A_str, count_F, a_str, ооо_222, ффф_222)
АБВГД = 10
print(АБВГД)