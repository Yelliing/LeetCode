def length_of_longest_substring(str, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = {}

    for window_end in range(len(str)):
        char_right = str[window_end]
        if char_right not in frequency_map:
            frequency_map[char_right] = 0
        frequency_map[char_right] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[char_right])

        # 如果window里的元素减去重复最多的元素 数值超过k
        # 那么我们就要缩小window size
        if (window_end - window_start + 1 - count) > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        print(f"<<<<< the window start is <<<<{window_start}")
        print(f"<<<<< the window end is <<<<{window_end}\n\n")
        max_length = max(max_length, window_end-window_start + 1)

    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))


main()
