
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


def fast_sliding_window(l, k):
    """
    we don't repeat addition which are not required. 
    to reuse the sum from the previous subarray, 
    we will subtract the element going out of the window and add the element now being included in the sliding window. 
    This will save us from going through the whole subarray to find the sum and, 
    as a result, the algorithm complexity will reduce to O(N).
    """

    window_sum, window_start = 0, 0
    window_sum_list = []

    for i in range(0, len(l)):
        window_sum += l[i]
        # the only loop will run till end of the list and only once. We never re-add any element.
        # check if window size matches with i; Once it matches we will keep the window size = k
        # and if will trigger every time i increases but k will keep window size constant.
        if(i >= k-1):
            print(i, window_sum_list)

            # append the result in our answer list
            window_sum_list.append(window_sum)
            # remove the element that move out of the window
            window_sum -= l[window_start]
            window_start += 1  # slide the window by one element
    print(window_sum_list)


fast_sliding_window([1, 2, 3, 4, 5, 6], 3)
