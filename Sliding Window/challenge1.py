def find_permutation(str, pattern):
    window_start = 0
    pattern_dic = {}
    matched = 0

    # setting up the dictionary for the string
    for chr in pattern:
        if chr not in pattern_dic:
            pattern_dic[chr] = 0
        pattern_dic[chr] += 1

    for window_end in range(len(str)):
        # extending the range of the window
        right_char = str[window_end]
        if right_char in pattern_dic:
            pattern_dic[right_char] -= 1
            if pattern_dic[right_char] == 0:
                matched += 1

        # if all characters have matched, reutrn true
        if matched == len(pattern_dic):
            return True

        # this statement is checking when window size is pattern size
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            # keep the window size at pattern size
            if left_char in pattern_dic:
                # 如果start是组成pattern的一部分， matched -1
                if pattern_dic[left_char] == 0:
                    matched -= 1
                pattern_dic[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))
    # this is the corner cases that i stuck on when first writing it myself
    print('Permutation exist: ' + str(find_permutation("cddbd", "dbc")))


main()
