# FACTORIAL CALCULATION USING RECURSION

# Step - 1 : Recursive Case - the flow | find the logic to implement recursion
# Step - 2 : Add a Base Case | Ensure that the base case is added
# Step - 3 : Unintentional Case  - the constraint | Identify the edge case and work on it


import sys

sys.setrecursionlimit(100)  # use the set recursion limit on code


def factorial(n):

    assert n >= 0 and int(n) == n, "The number must be a positive integer only"

    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


answer = factorial(10)
print(answer)

# Recursion example

# def openRussianDoll(doll):
#     if doll == 1:
#         print("All dolls are opened")
#     else:
#         openRussianDoll(doll-1)
#         print(f"doll {doll} opened")


# openRussianDoll(100)


# Important points to note :
# 1. Recursion holds on the code at 1 then goes to 2. It does this until it reaches
# boundary. So what happens is  once the boundary condition is proved, it starts moving back...
# from its boundary.So basically it prints the 100 before 1.

# Let me check if my understanding is correct
# Debugger start....

# def recursiveMethod(n):
#     if (n < 1):
#         print("n is less than 1")
#     else:
#         recursiveMethod(n-1)
#         print("number printed is : ", n)


# recursiveMethod(10)


# Well my hypothesis is wrong... it prints 1..
# but it loads 100 in memory, and that function is on hold.
# The FILO is actually working to deliver the result we are looking for....
