# Collection Deque

import collections
from collections import deque

d = deque("hello")
print(d)
d.append("ed")
d.append(6)
print(d)
d.appendleft(5)
print(d)

# using pop to remove elements at last or first
d = deque("hello")
d.pop()
d.popleft()

# Faster in adding elements in a list
d.extend(['1', '2'])
print(d)
# d.clear()
# print(d)

d.extendleft("Niko")
print(d)


# Rotate :  Takes an Integer and rotates value to the right on positive and left on negative

d.rotate(-1)
print(d)
d.rotate(-2)
print(d)
d.rotate(1)
print(d)
d.rotate(3)
print(d)

# Max Len

d = deque("hello", maxlen=5)
print(d)
d.append(1)
print(d)

# When the deque is specified of a maximum length using maxlen parameter and the deque has reached the maximum length, if an element is added to the left side one element is removed from the right side; when an element is added to the right side one element is removed from the left side.