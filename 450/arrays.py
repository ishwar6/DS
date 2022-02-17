my_str = 'A unicode \u018e \u1F6e string \xf1'
print(my_str)


def IsUnique(string) -> bool:
    if len(string) > 128:
        return False
    array = [False for i in range(128)]
    for i in string:
        if array[ord[i]]:
            return False
        array[ord[i]] = True
    return True


num1 = 0


def out_func():
    num1 = 1

    def in_func():
        nonlocal num1
        num1 = 2

    in_func()
    return num1


num2 = out_func()
print(num1, num2)


list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 == list3)
print(list1 is list3)
print(list1 == list2)
print(list1 is list2)


def my_func():
    s1 = 'CutShort'
    s2 = 'CutShort'
    s3 = 'CutShort'
    s4 = ''.join(['C', 'u', 't', 'S', 'h', 'o', 'r', 't'])

    return s1 is s2, s3 is s4


x, y = my_func()
print(x, y)

a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)


def my_func(nums):
    a, *b, c = nums
    return a, b


nums = [2, 4, 8, 10, 11]


a, b = my_func(nums)
print(a, b)

print("------")

circle_areas = [3.54773, 5.57778, 4.00014, 59.24241, 34.01344, 32.01013]

result = list(map(round, circle_areas, range(1, 3)))
print(result)


def my_func(s, z):
    total = 0
    len_str = len(s)

    for x, y in z:
        if x == 0:
            total += y
        else:
            total -= y
    total = total % len_str
    print(s[total:] + s[:total])


s = 'cutshort'
z = [[0, 3], [1, 11]]
my_func(s, z)

print("------")
x = "abcdef"
i = "a"
while i in x:
    print(i)
    x = x[1:]
    print(x)
    print(i, end=" ")


def oddsums(n):
    total = 0
    result = []
    for i in range(1, n+1):
        odd = 2*i-1
        total = total+odd
        result.append(total)
    return result


print(oddsums(5))
