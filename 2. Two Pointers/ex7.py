# Given an array with positive numbers and a target number,
# find all of its contiguous subarrays whose product is
# less than the target number.

from collections import deque


def find_subarrays(arr, target):
    arr.sort()
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]

        while (product >= target and left < len(arr)):
            product /= arr[left]
            left += 1
        # resets the deque to empty
        temp_list = deque()
        # 加一个元素到deque 然后加进 result
        # loop后再加一个元素到deque 加到result的deque就有两个元素
        # 反向的for循环所以用 appendleft把小的元素加在最前面
        # 这里注意 python特性 reverse loop 需要loop到 -1
        for i in range(right, left-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result


def main():
    print(find_subarrays([2, 5, 3, 10], 30))
    print(find_subarrays([8, 2, 3, 5], 50))


main()
