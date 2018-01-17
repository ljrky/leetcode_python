def twoSum(nums, target):
    dic = dict()

    for i, value in enumerate(nums):
        sub = target - value
        if sub in dic:
            return [dic[sub], i]
        else:
            dic[value] = i


result = twoSum([1, 2, 11, 15], 20)
print(result)
