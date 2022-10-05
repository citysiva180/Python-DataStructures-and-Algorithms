# Comprehensions

x = [1, 2, 3, 4, 5, 6, 5]

# A simple List comprehension
new = [i for i in range(10)]
print(new)

# Multiple for loops in a list comprehension

hello = [i*j for i in range(10, 20) for j in range(1, 10)]
print(hello)

# Generating 2D array

y = [[0 for _ in range(5)]for _ in range(5)]
print(y)

# _ is actually variable name. If you dont plan on using a single name
# For the variable then _ would work.


# List comprehension for prime numbers until hundred
prime_numbers = [x for x in range(2, 100) if all(
    x % y != 0 for y in range(2, x))]
print(prime_numbers)


# List comprehension for 3 Fibonacci and Fibonacci series
series = []
series.append(1)
series.append(1)
[series.append(series[k-1]+series[k-2]) for k in range(2, 5)]
print(series)
# Frequency counter with Dictionary comprehension
sentence = "The quick brown fox jumps over a lazy dog"
freq_counter = {char: sentence.count(char) for char in set(sentence)}
print(freq_counter)
