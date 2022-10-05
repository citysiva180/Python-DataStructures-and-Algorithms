import string

# alphas = string.ascii_lowercase
# print(list(alphas))

# # Generating number equivalent and zipping them...
# new_list = list(alphas)

# empty_dict = {}
# for items in range(len(new_list)):
#     empty_dict[new_list[items]] = items + 1

# print(empty_dict)


# def find_numerical_value(word):
#     sum_of_words = 0
#     for items in word:

#         sum_of_words += empty_dict[items]
#     return sum_of_words


# final = find_numerical_value("attitude")
# print(final)


# Making the code pythonic and simple...

alphas = list(string.ascii_lowercase)
alpha_dict = {alphas[items]: items + 1 for items in range(len(alphas))}

def find_numerical_value(word):
    sum_of_words = 0
    for items in word:

        sum_of_words += alpha_dict[items]
    return sum_of_words


final = find_numerical_value("attitude")
print(final)


# Best Practice

def words_to_marks(s):
    return sum(ord(c)-96 for c in s)


numerology = words_to_marks("sivarajan")
print(numerology)