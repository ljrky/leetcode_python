def reverse_integer(nums):
    z = nums if nums > 0 else -nums

    x = 0

    while z > 0:
        x = x * 10 + z % 10
        z = int(z / 10)

    if nums > 0:
        return x
    else:
        return -x


# test = 1234
test = -1000
result = reverse_integer(test)
print(result)
