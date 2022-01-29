from platform import python_branch


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


test()
