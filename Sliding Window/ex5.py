def fruits_into_baskets(fruits):
    window_start = 0
    max_fruit = 0
    fruit_numbers = {}

    for window_end in range(len(fruits)):
        # add fruits into the basket
        fruit_right = fruits[window_end]
        if fruit_right not in fruit_numbers:
            fruit_numbers[fruit_right] = 0
        fruit_numbers[fruit_right] += 1

        # shrink the window to only 2 types of fruit
        while len(fruit_numbers) > 2:
            fruit_left = fruits[window_start]
            fruit_numbers[fruit_left] -= 1
            if fruit_numbers[fruit_left] == 0:
                del fruit_numbers[fruit_left]
            window_start += 1
        max_fruit = max(max_fruit, window_end-window_start + 1)
    return max_fruit


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
