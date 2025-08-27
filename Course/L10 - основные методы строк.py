s = "Python для автоматизации"
print(s.upper())
print(s.lower())
msg = "абракадабра"
print(msg.count('ра'))
print(msg.count('а',  3))
print(msg.find("ка"))
print(msg.find("а", -1))
print(msg.find("xyz"))
text = "Я изучаю Java"
print(text.replace("Java", "Python"))
print(text.replace(" ", ""))
t = "Python"
print(t.isalpha())
t2 = "12345"
print(t2.isdigit())
t3 = '123abc'
print(t3.isdigit())
code = "42"
print(code.rjust(7, '0'))
text = "text"
print(text.ljust(10, "*"))
a = "яблоко, груша, банан"
print(a.split(", "))
b = "Python;Java;C++"
print(b.split(';'))
c = "Привет", "мир", "!"
print(" ".join(c))
d = "apple", "banana", "cherry"
print(", ".join(d))
i = " Python "
print(i.lstrip())
print(i.rstrip())
print(i.strip())
text = "программирование"
text2 = 'П' + text[1:]
print(text2)
print(text2.count('р'))
print(text2.find('и', 0, 10))
ooo = text2[::-1]
print(ooo)
print(ooo.find('и', 0, 10))

text = "программирование"
print(text.capitalize())     # 'Программирование' - сделать заглавной первую букву capitalize


