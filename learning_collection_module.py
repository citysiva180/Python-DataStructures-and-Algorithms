# Collections Module


# import collections
from collections import Counter

# Its a built in module for having different datatypes

# Containers

# List
# Set
# Dict
# Tuple

# Types

# Counter
# deque
# namedTuple()
# orderedDict
# DefaultDict

# In this first section we would be checking out counter
c = Counter("Gallad")
print(c)
e = Counter(['a', 'a', 'b', 'c', 'c'])
print(e)
d = Counter({'a': 4, 'b': 6})
print(d)
f = Counter(cats=4, dogs=7)
print(f)


para = Counter("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lore Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
""")

# Count Occurnce of characters
print(para)

# Element functions

# Simply prints all the elements in the sentence or string without  removing duplicates

# print(list(para.elements()))

# Most Common
print(para.most_common(2))


# Subtracting values
# you could keep a

n = Counter(a=4, b=2, c=0, d=-4)
g = ['a', 'b', 'c', 'd']
n.subtract(g)
print(n)

# Updating Values
# you could easily update values in your dictionary using this option

k = ['a', 'd', 'f', ',l', 'h']
n.update(k)
print(n)

# Using Arithematic Expressions with the counter function
p = Counter(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
print("Addition")
print(p + n)
print("Subtraction")
print(p - n)

# Union and Intersection
print("Union")  # Takes a maximum elements
print(p | n)
print("Intersection")  # Takes the minimum elements
print(p & n)


# Removing all values in the counter
n.clear()
print(n)
