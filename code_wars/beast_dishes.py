# beast dishes where the animal name and the dish name should be the same. as in starting and ending
def feast(beast, dish):

    final = True if (beast[0] == dish[0] and beast[-1] == dish[-1]) else False
    return final


print(feast("brown bear", "bear claw"))
print(feast("great blue heron", "garlic naan"))

# Another readable way of writing code for checking front end back


def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])


# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

def powers_of_two(n):
    n_new = n+1
    final = [(2)**x for x in range(n_new)]
    return final


print(powers_of_two(0))
print(powers_of_two(1))
print(powers_of_two(4))

# Single line


def powers_of_two(n): return [2 ** i for i in range(n+1)]

