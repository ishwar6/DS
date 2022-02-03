# Given a string, find the length of the longest substring in it with no more than K distinct characters
# use a HashMap to remember the frequency of each character we have processed


def longest_substring_with_k_distinct_character(str, k=0):

    window_start, window_end, max_length = 0, 0, 0
    frequency_char = {}

    for window_end in range(len(str)):
        temp_char = str[window_end]
        if temp_char not in frequency_char:
            frequency_char[temp_char] = 0
        frequency_char[temp_char] += 1

        while len(frequency_char) > k:
            remove_char = str[window_start]
            frequency_char[remove_char] -= 1
            if frequency_char[remove_char] == 0:
                del frequency_char[remove_char]
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    print(max_length)
    return max_length

"""
The time complexity of the above algorithm will be O(N)
The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
"""


longest_substring_with_k_distinct_character("araaci", k=2)
longest_substring_with_k_distinct_character("araaci", k=1)
