# Generators in python
import sys
# Iterators are functions which enumerates through a list without memory

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# In a traditional method, you need to save the number in a list and that gets stored in memory

# print(sys.getsizeof(x))

# for element in x:
#     print(element)

# for elements in range(1, 11):
#     print(elements)

# print(sys.getsizeof(range(1, 11)))


y = map(lambda i: i**2, range(1, 11))
# print(list(y))

# the Next function its an important function which
# helps in finding the next value, since only
# iterators could do this for you...

print(next(y))
print(next(y))
print(next(y))
print(next(y))

# you also have a dunder method for the same

print(y.__next__())


while True:
    try:
        value = next(y)
    except StopIteration:
        print('Done')
        break

# you could also use the iter function to iterate through the values
# in the code.

x = range(1, 11)
print(next(iter(x)))
print(x.__iter__())

# Defining the iterator


# class Iter:
#     def __init__(self, n):
#         self.n = n

#     def __iter__(self):
#         self.current = 0
#         return self

#     def __next__(self):
#         self.current += 1
#         if self.current >= self.n:
#             raise StopIteration

#         return self.current


# z = Iter(5)
# for i in z:
#     print(i)

# Important, Remember the

def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)

# Remember
numbers  = range(1,100)
def generate_nums(numbers):
    for rows in numbers:
        yield(rows)

gen = generate_nums(numbers)
print(next(gen))



# Generator Comprehensions
x = (i for i in range(10))
print(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
