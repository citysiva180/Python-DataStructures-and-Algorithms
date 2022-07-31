# Asynchronous programming with Python
# Topics Covered
#   - Co-Routines, Tasks, Future, Await, Async , AsyncIO Module

import asyncio

# An Example of Sync Programming


def foo():
    return


foo()
print('tim')

# Async is the option for other code to work while 1 program is working on its task and does not affect others

# Co_routine : A Wrapped version of function for running async code

# ON calling a co-routine object will be called

# The Await keyword should be inside async function

# Event loop is a block for writing async code


async def main():
    print("Tim")
    await foo('text')
    print('finished')


async def foo(text):
    print(text)
    await asyncio.sleep(1)
    print("finished")

asyncio.run(main())

print("")
print("")
print("")
print("")


async def main_1():
    print("Tim")
    task = asyncio.create_task(foo_1('text'))
    print('finished')


async def foo_1(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main_1())
