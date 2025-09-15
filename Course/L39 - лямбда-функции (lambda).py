# Задание 1:

square = lambda num: num ** 2
print(square(5))

# Задание 2:

is_even = lambda num: num % 2 == 0

print(is_even(4))
print(is_even(7))

# Задание 3:

numbers = [1, 2, 3, 4]
square_list = list(map(lambda x: x ** 2, numbers))

print(square_list)

# Задание 4:

nums = [-3, 0, 5, -8, 10]
positive_numbers = list(filter(lambda x: x > 0, nums))

print(positive_numbers)

# Задание 5:

words = ["banana", "apple", "cherry"]
sort_by_last_letter = sorted(words, key=lambda word: word[-1])
print(sort_by_last_letter)