def pair_with_targetsum(arr, target_sum):

    left_pointer = 0
    right_pointer = len(arr) - 1
    while left_pointer <= right_pointer:
        if arr[left_pointer] + arr[right_pointer] > target_sum:
            right_pointer -= 1
        elif arr[left_pointer] + arr[right_pointer] < target_sum:
            left_pointer += 1
        else:
            return[left_pointer, right_pointer]

    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
