def searchInsertPosition(nums, value):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = int((right - left) / 2) + left
        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else :
            right = mid - 1

    return left


test_set = [1, 2, 2, 3, 6, 8, 9]
result = searchInsertPosition(test_set, 10)
print(result)
print(test_set)
