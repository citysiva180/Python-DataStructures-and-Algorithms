# Map function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def func(x):
    return x ** x


print(list(map(func, li)))

num = func()
print(num)


# Use the map function to improve your syntax 
org_list = [1, 2, 3, 4, 5]
fin_list = list(map(lambda x:x**3, org_list))
print(fin_list)