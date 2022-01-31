
def sliding_window_brute_force(l, k):
    """
    l is the array of integers and k is window size.
    Let l = [1, 2, 3, 4, 5, 6] and window size k is 3
    size of l = 6
    Outer for loop should run till element 4: index = 3
    so range(0,4) = 0,1,2,3 (will run till 3)
    so we run range till len(l) - k + 1
    1 is needed because last element is not counted in range. 
    """
   # print(l,k)

    for i in range(len(l)-k+1):
        s = 0
        for j in range(i, i+k):
            s = s + l[j]
        print(s)


# sliding_window_brute_force([1, 2, 3, 4, 5, 6], 3)
# 6
# 9
# 12
# 15

# time complexity is O(N*K) ( n is list size and k is window size )
