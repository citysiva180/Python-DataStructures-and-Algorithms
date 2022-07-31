# In this section we would be dealing with multiple Topics Such as

# Default dictionary
# Counter
# Deque
# NamedTuple
# Chain Map
# OrderedDict


# Default dictionary helps in initiating a
# dictionary without any keys
# A normal dictionary will be empty without keys
# But a default dictionary will assign keys automatically

from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
nums['three'] = 3
print(nums['four'])

# Even though num 4 is not there, 
# default dict will  assign a 