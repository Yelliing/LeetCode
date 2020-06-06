# given two strings containing backspaces (identified by teh character #), check
# if the two strings are equal


def backspace_compare(str1, str2):
    pt1 = len(str1) - 1
    pt2 = len(str2) - 1
    longer = max(len(str1), len(str2))
    while(pt1 > -1 and pt2 > -1):
        if str1[pt1] == "#":
            pt1 -= 2
        if str2[pt2] == "#":
            pt2 -= 2
        if str1[pt1] == str2[pt2]:
            continue
        else:
            return False

    return True


def main():
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
