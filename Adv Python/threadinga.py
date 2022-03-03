# A1, A2, A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15]
# Output – [A1,A15,A2,A3,A14,A4,A5,A6,A13,A7,A8,A9,A10,A12,A11].
# Sample Input – [2,5,9,10,45,2,34,13,49,20,].
# Output – [2,20,5,9,49,10,45,2,13,34].

def list_print(mylist):
    l, r = 1, len(mylist)
    res = []
    prev = 0
    res.append(mylist[0])

    for i in range(1, len(mylist)):
        r -= 1
        if len(res) <= len(mylist):
            res.append(mylist[r])

        # increment l by i units
        prev = l
        l = l + i+1
        # print(prev, l)
        if l < len(mylist) and len(res) < len(mylist):
            for k in range(prev, l):
                res.append(mylist[k])

        # decrease j by one unit
    return res


a = list_print(list(range(1, 31)))
print(a)


# Msg(Msg_id, user_id, text, file, timestamp)

# OneToOneChat(user_id_1, user_id_2, timestamp, Msg_id)

# GroupChat(GroupChat_id, list_of_user_ids, host_user_id, Msg_id, timestamp)

# State(User_id, GroupChat_id, is_active, is_muted)

# GroupMsg(GroupChat_id, Msg_id)

# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(arr, low, high):
    i = (low-1)		 # index of smaller element
    pivot = arr[high]	 # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort


def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
