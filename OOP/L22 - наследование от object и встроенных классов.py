# Задание 1: класс ResultList на основе list

class ResultList(list):
    def success_count(self):
        return sum(1 for item in self if item.get("status") == "passed")

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count()) # 2

# Задание 2: проверка issubclass() и isinstance()

class BaseStep:
    pass

class LoginStep(BaseStep):
    pass

step = LoginStep()

print(issubclass(LoginStep, BaseStep)) # True
print(isinstance(step, BaseStep)) # True
print(isinstance(step, object)) # True

# Задание 3: переопредели __str__ у класса ExtendedDict

class ExtendedDict(dict):
    def __str__(self):
        return "\n".join(f"{k}: {v}" for k, v in self.items())

d = ExtendedDict(a=1, b=2)
print(d)