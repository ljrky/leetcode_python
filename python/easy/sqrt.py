def sqrt(x):
    y = 1
    precision = 0.0001
    while abs(y * y - x) > precision:
        y = (y + x / y) / 2

    return int(y)


test = 15
result = sqrt(test)
print(result)

a = 'a'
print(len(a))