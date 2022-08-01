# A decorator in Python is a function that takes another function as its argument, and returns yet another function . Decorators can be extremely useful as they allow the extension of an existing function, without any modification to the original function source code.
import math


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Something is going on here...")
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, orginal_function):
        self.orginal_function = original_function

    def __call__(self, *args, **kwargs):
        print(
            "Call method executed this before {self.original_function.__name__}")


@decorator_function
def say_hi_and_bye():
    print("Hi, How are you?")


say_hi_and_bye()
# is Same as

hi_func = decorator_function(say_hi_and_bye)
hi_func()


@decorator_class
# Decorator function with
def display_info(name, age):
    print(f'display_info ran with arguments {name} {age}')


display_info('John', 25)
