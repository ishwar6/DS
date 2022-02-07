
def print_r(n):
    if(n == 1):
        print(1)
        return 1
    print(n)
    print_r(n-1)


# print_r(4)


def print_r(n):
   # print("UP for", n)
    if(n == 1):
        print(1)
        return 1

    print_r(n-1)
    print("here for", n)

    print_r(n-1)


print_r(3)
