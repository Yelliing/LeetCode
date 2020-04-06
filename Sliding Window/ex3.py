import math


def smallest_subarray_with_given_sum(s, arr):
    minLength, currentSum = math.inf, 0
    windowStart = 0

    for windowEnd in range(len(arr)):
        currentSum += arr[windowEnd]  # add the next element
        # get rid of front elements as much as possible using while loop
        while currentSum >= s:
            minLength = min(minLength, windowEnd - windowStart + 1)
            currentSum -= arr[windowStart]
            windowStart += 1
    if minLength == math.inf:
        return 0
    return minLength


def main():
    array = [2, 1, 5, 1, 3, 2]
    result = smallest_subarray_with_given_sum(7, array)
    print("The smallest subarray with a sum greater than 7 is size: " + str(result))


main()
