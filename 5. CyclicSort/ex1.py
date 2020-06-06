def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1  # this records the intended index of the number at index i
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:  # the index pushes forward as the number gets in place
            i = i + 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
