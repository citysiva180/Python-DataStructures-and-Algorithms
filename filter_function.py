# Filter function

def add_7(x):
    return x+7


def isOdd(x):
    return x % 2 != 0


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Pass a function and a iterable so the function will filter out the add numbers
b = list(filter(isOdd, a))
print(b)

# Map + Filter combo

c = list(map(add_7, b))
print(c)


d = list(map(add_7, filter(isOdd, a)))
print(d)
