# Given a string, find the length of the longest substring which has no repeating characters.

# We can use a HashMap to remember the last index of each character we have processed.
#  Whenever we get a repeating character we will shrink our sliding window
#  to ensure that we always have distinct characters in the sliding window.


# aabcbd => abc (3)
def longest_substring(str):
    window_start, window_end, max_length = 0, 0, 0
    frequency_char = {}

    for window_end in range(len(str)):

        temp_char = str[window_end]

        if temp_char in frequency_char:
            # slide the window
            # Move window_end to next character of string from where temp_char was previously present.
            # It might happen that previously temp_char was found but it DNE between window_start and window_end. So max is taken.
            print(frequency_char)
            window_end = max(frequency_char[temp_char]+1, window_end)
            frequency_char[temp_char] = window_end

            if window_end-window_start > max_length:
                print("MAX", max_length, window_start, window_end)
                max_length = window_end-window_start
                result_string = str[window_start:window_end]
            window_start += 1

        else:
            # increase the max_length and add the character with its position

            frequency_char[temp_char] = window_end
    print(max_length, result_string)
    return max_length


# longest_substring("aaasdpfeasdfaaa")  # 6 asdpfe

# {'a': 0}
# MAX 0 0 1
# {'a': 1}
# {'a': 2, 's': 3, 'd': 4, 'p': 5, 'f': 6, 'e': 7}
# MAX 1 2 8
# {'a': 8, 's': 3, 'd': 4, 'p': 5, 'f': 6, 'e': 7}
# {'a': 8, 's': 9, 'd': 4, 'p': 5, 'f': 6, 'e': 7}
# {'a': 8, 's': 9, 'd': 10, 'p': 5, 'f': 6, 'e': 7}
# {'a': 8, 's': 9, 'd': 10, 'p': 5, 'f': 11, 'e': 7}
# {'a': 12, 's': 9, 'd': 10, 'p': 5, 'f': 11, 'e': 7}
# {'a': 13, 's': 9, 'd': 10, 'p': 5, 'f': 11, 'e': 7}
# 6 asdpfe


# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string.
# Space complexity is O(1): Max 26 elements can come in hashmap
#  we can use a fixed-size array instead of the HashMap.

def non_repeat(str):
    window_start = 0
    max_length = 0
    char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str)):
        right_char = str[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
        print(char_index_map, right_char)
        if right_char in char_index_map:
            print("INSIDE", window_start, char_index_map[right_char]+1)
            window_start = max(window_start, char_index_map[right_char]+1)
        char_index_map[right_char] = window_end
        max_length = max(max_length, window_end-window_start+1)
    return max_length


a = non_repeat("aabcas")
print(a)
