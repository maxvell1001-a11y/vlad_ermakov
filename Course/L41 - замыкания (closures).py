# Задание 1:

def multiply_by(n):
    def mult_in(x):
        return x * n
    return mult_in

times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))
print(times5(10))

# Задание 2:

def counter(start=0):
    def counter_in():
        nonlocal start
        start += 1
        return start
    return counter_in

c1 = counter(5)
c2 = counter()

print(c1())  # 6
print(c1())  # 7
print(c2())  # 1
print(c2())  # 2

# Задание 3:

def word_filter(forbidden_words):
    def check(text):
        return any(word in text.lower() for word in forbidden_words)
    return check

bad_words = word_filter(["spam", "fake", "scam"])

print(bad_words("This is a scam!"))
print(bad_words("This is a test."))

# Задание 4:

def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip

strip1 = strip_string()
strip2 = strip_string("!?.")

print(strip1("  hello python  "))
print(strip2("!!hello python!!!"))