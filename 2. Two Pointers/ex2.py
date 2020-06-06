def remove_duplicates(arr):
    next_non_duplicate = 1

    for next in range(1, len(arr)):
        if arr[next_non_duplicate - 1] != arr[next]:
            arr[next_non_duplicate] = arr[next]
            next_non_duplicate += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
