def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    for window_end in range(len(str)):
        # first add as much element as possible into the dictionary
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        # shrink the dictionary until the window has only k dinstinct
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        # remember the max_length so far
        max_length = max(max_length, window_end-window_start + 1)

    return max_length


def main():
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))


main()
