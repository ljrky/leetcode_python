def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        if digits[i] < 9:
            digits[i] = digits[i] + 1
            return digits
        else:
            digits[i] = 0
        i = i - 1

    digits.insert(0,1)
    return digits

test = [9]
result = plusOne(test)
print(result)
