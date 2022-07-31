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
