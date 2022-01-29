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
# t = int(input())
# while t:
#     n, m = map(int, input().split())
#     print(n, m)


def gcd(a, b):
    print("Calling Euclid Division Lemma for", a, b)
    if a == 0:
        print("GCD is ", b)
        return b
    else:
        return gcd(b % a, a)


#print(gcd(225, 135))


def lcm(a, b):
    product = a*b
    hcf = gcd(a, b)
    return product//hcf


#print(lcm(2, 0))


def strike(text):
    """ Renders string with strike-through characters through it.

        `strike('hello world')` -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'

        Notes
        -----
        \u0336 is a special strike-through unicode character; it
        is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)


# a = strike("aadfdaf")
# print(a)


class ShoppingList:
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with
            purchased items being crossed out.

            Returns
            -------
            str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply
            # googled "unicode bullet point" and copied/pasted it here.
            return "• " + "\n• ".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)


l = ShoppingList(["grapes", "beets", "apples", "milk", "melon", "coffee"])
l.mark_purchased_items(["grapes", "beets", "milk"])
print(l)
