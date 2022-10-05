# Creating Anonymous functions with python (Lambda)

def func(x):
    return x + 5


def func2(x): return x+5/4


def func3(x): return x+5/2


print(func(2))
print(func3(3))

a = [1, 2, 3, 4, 5, 6]

newList = list(filter(lambda x: x % 2 == 0, a))
print(newList)

# Combo your lambda with filter or map to quickly build an expression
