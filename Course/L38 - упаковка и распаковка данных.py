# Задание 1:

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(10, 20, 30))

# Задание 2:

def print_info(name, age, **kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        print(f"Имя: {name}")
        print(f"Возраст: {age}")

print_info("Алексей", 25, город="Москва", профессия="Программист")

# Задание 3:

def merge_lists(*lists):
    return [*lists[0], *lists[1], *lists[2]]

print(merge_lists([1, 2], [3, 4], [5, 6]))

# Задание 4:

def merge_dicts(*dicts):
    return {**dicts[0], **dicts[1], **dicts[2]}

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}

print(merge_dicts(d1, d2, d3))

# Задание 5:

def unpack_list(lst):
    first, *rest = lst
    return first, rest

print(unpack_list([10, 20, 30, 40]))