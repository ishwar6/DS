# Given a string, find the length of the longest substring which has no repeating characters.


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


longest_substring("aaasdpfeasdfaaa")  # 6 asdpfe

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
