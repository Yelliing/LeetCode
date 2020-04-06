def non_repeat_substring(str):
    window_start = 0
    longest_substring = ""
    max_length = 0

    for window_end in range(len(str)):
        char_right = str[window_end]  # the right pointer to the string
        # shrink the window size
        while char_right in longest_substring:
            longest_substring = longest_substring[1:]
        window_start += 1
        #  add elements to the substring
        if char_right not in longest_substring:
            longest_substring += char_right
        max_length = max(max_length, len(longest_substring))
    return max_length


def main():
    print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
