# TOPIC-1: ITERABLES and MAP

# list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
# Under the hood”, an iterable is any Python object with an __iter__() method or with a __getitem__() method that implements Sequence semantics.
# sum(), sorted(), any(), all(), max(), min() are functions defined over iterable.


# map(func, iter) in python
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.


def addition(n):
    return n + n


def test():
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    #result = map(lambda x: x+x, numbers)
    print(result)
    print(list(result))


# test()

# assigning contents of a list to variables using iterable unpacking
my_list = [7, 9, 11]

x, y, z = my_list
# print(x, y, z) #7 9 11


# The built-in enumerate function allows us to iterate over an iterable, while keeping track of the iteration count:
# In general, the enumerate function accepts an iterable as an input, and
# returns a new iterable that produces a tuple of the iteration-count and the corresponding item from the original iterable.

# The built-in enumerate function should be used (in conjunction with iterator unpacking) whenever it is necessary to track the iteration count of a for-loop.
# It is valuable to use this in conjunction with tuple unpacking.


# using the `enumerate` function to keep iteration-count
# Enumerate returns tuple if unpacked.
none_indices = []

# note the use of iterable unpacking!
for iter_cnt, item in enumerate([2, None, -10, None, 4, 8]):
    if item is None:
        none_indices.append(iter_cnt)

# `none_indices` now stores: [1, 3]
