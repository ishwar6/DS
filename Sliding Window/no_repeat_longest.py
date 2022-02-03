# Given a string, find the length of the longest substring which has no repeating characters.


# aabcbd => abc (3)
def longest_substring(str):
    window_start, window_end, max_length = 0, 0, 0
    frequency_char = {}

    for window_end in range(len(str)):

        temp_char = str[window_end]
        if temp_char in frequency_char:
            # slide the window

            if window_end-window_start > max_length:
                max_length = window_end-window_start+1
                result_string = str[window_start:window_end]
            window_start += 1

        else:
            # increase the max_length and add the character
            max_length += 1
            frequency_char[temp_char] = 1
