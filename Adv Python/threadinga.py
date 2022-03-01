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
    t = asyncio.create_task(foo())

    print("finished")
    await t


async def foo():
    await asyncio.sleep(5)
    print("foooo")


# asyncio.run(main())

# import math
# l,r = 0,0
# window_sum = 0
# min_length = math.inf

# for r in range(len(A)):
#     window_sum = window_sum + A[r]

#     while window_sum >= target_sum:
#         min_length = min(min_length, r-l+1)
#         window_sum = window_sum - A[l]
#         l = l-1

# #check condition if min_length never get updated
# if min_length == math.inf:
#     return 0
# return min_length


def k_distinct(A: str, k: int):
    l, r, window_sum, max_l = 0, 0, 0, 0
    hash_dict = {}

    for r in range(len(A)):
        current_char = A[r]
        hash_dict[current_char] = hash_dict.get(current_char, 0) + 1

        while len(hash_dict) > k:
            left_char = A[l]
            hash_dict[left_char] -= 1
            l += 1
            if hash_dict[left_char] == 0:
                del hash_dict[left_char]
        print(max_l, l, r)
        max_l = max(max_l, r-l+1)
    return max_l


# a = k_distinct("cbbebi", 3)
# print(a)

stats = {'a': 1000, 'b': 3000, 'c': 100}
print(max(stats))
