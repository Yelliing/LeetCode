def find_max_subarray(arr, K):
    maxSum, currentSum = 0, 0
    windowStart = 0
    for windowEnd in range(len(arr)):
        currentSum += arr[windowEnd]
        if windowEnd >= K-1:
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def main():
    array = [2, 1, 5, 1, 3, 2]
    result = find_max_subarray(array, 3)
    print("The max sub arry with size 3 is: " + str(result))


main()
