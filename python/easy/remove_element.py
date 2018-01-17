def removeElement(num, value):
    index = 0
    for i in range(0, len(num)):
        if num[i] != value:
            num[index] = num[i]
            index = index + 1
    return index


# test_set = [2, 1, 1, 1, 1, 1, 1, 2]
test_set = [3,2,2,3]    
result = removeElement(test_set, 3)
print(result)
print(test_set)
