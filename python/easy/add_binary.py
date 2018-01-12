def addBinary(a,b):
    # if a is 0
    if a == '':
        return b

    # if b is 0
    if b == '':
        return a

    # if last a and last b is both 1:
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[:-1], b[:-1]), '1') + '0'

    # else if last a is 1 or last b is 1:
    elif a[-1] == '1' or b[-1] == '1':
        return addBinary(a[:-1], b[:-1]) + '1'

    # else if last a and last b is both 0
    else:
        return addBinary(a[:-1], b[:-1]) + '0'

test = '11'
test2 = '1'
result = addBinary(test, test2)
print(result)