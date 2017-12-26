def reverse_integer(nums):
    if nums < 0:
        return False
    else:
        test = nums
        result = 0
    while test > 0:
        result = result * 10 + test % 10
        test = int(test / 10)
    return result


def isPalindromeNumber(nums):
    result = reverse_integer(nums)
    if result == nums:
        return True
    else:
        return False


print(isPalindromeNumber(323))
print(isPalindromeNumber(2222))
print(isPalindromeNumber(1234))
