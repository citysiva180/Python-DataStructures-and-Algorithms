# Names Tuple

import collections
from collections import namedtuple

point = namedtuple('point', 'x,y,z')
new_point = point(3, 4, 5)
print(new_point)
