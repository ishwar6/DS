import asyncio
from threading import *


def display():
    for i in range(10):
        print("child thread")


t = Thread(target=display)
# t.start()


def display_p():
    for i in range(10):
        print("main thread")


# display_p()


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)


async def main():
    print('hi')


async def foo():
    print("foooo")
print(foo())
asyncio.run(main())
