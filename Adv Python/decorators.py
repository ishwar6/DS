global top
top = -1
my_list = []


def enque(my_list, data, top):

    my_list.append(data)
    top += 1
    return my_list


def deque(my_list, top):
    length = top
    if top == 0:
        top -= 1
        return my_list[0]

    if top == -1:
        return None

    temp = []

    while length >= 0:
        temp_top = my_list[length]
        temp.append(temp_top)
        length -= 1
    data = temp[len(temp)-1]
    print(temp)
    my_list = temp[::-1]
    print(my_list)
    top -= 1
    return data


enque(my_list, 1, 0)
enque(my_list, 12, 1)
enque(my_list, 14, 2)
deque(my_list, 1)
print(my_list, 0)
