# 1. Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five.

import collections as col


def find_numbers(num_list):
    if (19, 5 in num_list):
        new_arr = col.Counter(num_list)
        final = True if new_arr[19] >= 3 or new_arr[5] >= 3 else False
    else:
        final = False
    return final


option_1 = [19, 19, 15, 5, 3, 5, 5, 2]
option_2 = [19, 15, 15, 5, 3, 3, 5, 2]
option_3 = [19, 19, 5, 5, 5, 5, 5]

print(find_numbers(option_1))
print(find_numbers(option_2))
print(find_numbers(option_3))

# Minifying the solution....
