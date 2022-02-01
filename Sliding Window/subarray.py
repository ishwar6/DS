# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

def max_subarray(arr, k):
    '''
    [1,2,3,4,5,6]
    Time Complexity
        The time complexity of this algorithm will be O(N).

    Space Complexity
        The algorithm runs in constant space O(1).
    '''
    window_start, window_sum, result_index = 0, 0, 0
    window_max = 0

    for i in range(0, len(arr)):
        window_sum += arr[i]
       # print(window_sum)

        if(i >= k-1):
            if(window_max < window_sum):
                window_max = window_sum
                result_index = i
            window_sum -= arr[window_start]
            window_start += 1

        """
        To slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:

         1. Subtract the element going out of the sliding window i.e., subtract the first element of the window.
         2. Add the new element getting included in the sliding window i.e., the element coming right after the end of the window.
         This approach will save us from re-calculating the sum of the overlapping part of the sliding window.

        """
    print("Max sum is", window_max)

    for j in range(result_index-k+1, result_index+1):
        print(arr[j])

        pass


# max_subarray([2, 1, 5, 1, 3, 2], 3)  # [5,1,3] with sum 9
# max_subarray([2, 3, 4, 1, 5], 2)  # [3,4] with sum 7

 # Variable Window Size: smallest contiguous subarray whose sum is greater than or equal to given target ‘S’


def smallest_subarray_with_given_sum(arr, s):
    i, window_end, window_sum, result_sum = 0, 0, 0, 0
    min_window_size = 9900000000

    while(i <= len(arr)):

        if(window_sum >= s):

            if(min_window_size > i-window_end):
                #    print("sizeee", i, window_end)
                min_window_size = i-window_end
                result_sum = window_sum
          #  print("SUM", window_sum, arr[window_end])
            window_sum -= arr[window_end]
            window_end += 1
        #    print("size", min_window_size, window_end)
        else:
           # print("i is", i)
            if(i > len(arr)-1):
                break
            window_sum += arr[i]
            i += 1
    print(min_window_size, result_sum)

    return -1


smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8)
smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)
smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7)
