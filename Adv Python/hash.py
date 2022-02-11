# Python hash() function is a built-in function and returns the hash value of an object if it has one.
# The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary.

# Syntax : hash(obj)
# Parameters :  obj : The object which we need to convert into hash.
# Returns : Returns the hashed value if possible.


# MUTABLE TYPE LIKE LIST, SET, DICT CAN'T BE HASHED.

# property of hash()

# initializing objects
# tuple are immutable
tuple_val = (1, 2, 3, 4, 5)

# list are mutable
list_val = [1, 2, 3, 4, 5]

# Printing the hash values.
# Notice exception when trying
# to convert mutable object
#print("The tuple hash value is : " + str(hash(tuple_val)))
# print("The list hash value is : " + str(hash(list_val)))  # TypeError: unhashable type: 'list'


# Here we will override the __hash()__ methods to call the hash(), and __eq__() method will check the equality of the two custom objects.

class Emp:
    def __init__(self, emp_name, id):
        self.emp_name = emp_name
        self.id = id

    def __eq__(self, other):

        # Equality Comparison between two objects
        return self.emp_name == other.emp_name and self.id == other.id

    def __hash__(self):

        # hash(custom_object)
        return hash((self.emp_name, self.id))


emp = Emp('Ragav', 12)
print("The hash is: %d" % hash(emp))

# We'll check if two objects with the same
# attribute values have the same hash
emp_copy = Emp('Ragav', 12)
print("The hash is: %d" % hash(emp_copy))


# Enumerate
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

# print("Return type:", type(obj1))
# print(list(enumerate(l1)))
# Return type: < class 'enumerate' >
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]


# changing start index to 2 from 0
# print(list(enumerate(s1, 2)))
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]


def test():
    # Python program to illustrate
    # enumerate function in loops
    l1 = ["eat", "sleep", "repeat"]

    # printing the tuples in object directly
    for ele in enumerate(l1):
        print(ele)

    # changing index and printing separately
    for count, ele in enumerate(l1, 100):
        print(count, ele)

    # getting desired output from tuple
    for count, ele in enumerate(l1):
        print(count)
        print(ele)


# [4,2,3,1,1,2,4,2,2]
# 4, 2
# 2,4


def print_count(number):
    number_dict = [[i, number.count(i)] for i in set(number)]

    # for i in number:
    #     number_dict[i] = number.count(i)

    print(number_dict)


#print_count([4, 2, 3, 1, 1, 2, 4, 2, 2])

# input - 1000 x 2000
# max reso - 500 x 500
# output - 250 x 500
# 500,1000
# 250,500
l = [1, 2]
l2 = l
l2[1] = 's'
print(l, l2)
# id(l)==id(l2)

# Student.objects.all()

# def same_aspect_ratio(x, y):
#     X_MAX = 500
#     ratio = x/y
#     print(ratio)
#     if ratio > 1:
#         temp_x, temp_y = X_MAX, X_MAX/ratio
#     else:  # x is smaller
#         temp_x, temp_y = X_MAX*ratio, X_MAX

#     print(temp_x, temp_y)


# same_aspect_ratio(1080, 1920)


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    print(char_set)
   # print(char_set)
    for char in string:
        val = ord(char)
        if char_set[val]:
            print(char_set[val])
            # Char already found in string
            return False
        char_set[val] = True
    print(char_set)

    return True


a = dict(name="ishwar", class_="a")
for i in a.items():
    print((i))


#     ('name', 'ishwar')
# ('class_', 'a')


# print(unique("Abcsd"))

s = set([1, 2, 3, 4, 5, 3, 2, 2])


a = set(['a', 'b'])
print(a.intersection(['a']))
