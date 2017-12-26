def removeDuplicates(nums):
    if not nums:
        return 0
    index = 0
    for i in range(1, len(nums)):
        if nums[index] != nums[i]:
            index = index + 1
            nums[index] = nums[i]

    return index + 1


test_set = [1, 1, 1, 1, 1, 1, 2]
result = removeDuplicates(test_set)
print(result)
print(test_set)
