# l = (44, 55)


# def add_emp(ages, age):
#     pass


# def add():
#     pass


# my_list = [2, 3, 4, 5, 6, 7]
# def my_fun(my_list): return my_list[:2]


# print(my_list[:2])
# print(my_list[2:4])
# print(my_list[4:])


# ages = (22, 33, 24)
# add_emp(ages, 44)


# # array of ints
# largest int smaller or equal then i


l = [1, 2, 3, 4, 5, 6]
length = len(l)
for i in range(int(length/2)):
    temp = l[i]
    l[i] = l[length-i-1]
    l[length-i-1] = temp

print(l)


# def get_smaller_than_i(l, i):
#     l.sort()
#     if l:
#         for k in l:


# def get_smaller_than_i(l, i):
#     res = filter(lambda k: k < i, l)
#     return max(res)


# max_v = -1000000
# num = 9
# for current in l:
#     if max_v < current and current < num:
#         max_v = current

# print(max_v)

# print(get_smaller_than_i(l, i))

class className(ParentClass):
