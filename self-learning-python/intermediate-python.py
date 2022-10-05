# # Optional parameters
# def func(x):
#     return x ** 2


# call = func(2)
# print(call)


# def func_1(x=1):
#     return x ** 2


# call = func_1()
# print(call)


import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.__repr__())
print(p.area()) #Static Method

print(Pizza.circle_area(4)) #Class Method

class person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult():
        return 5 >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')
