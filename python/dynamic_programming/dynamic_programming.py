def dynamicProgramming(steps):
    if steps < 1:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2

    step1 = 1
    step2 = 2
    temp = 0

    for i in range(3, steps + 1):
        temp = step1 + step2
        step1 = step2
        step2 = temp

    return temp


print(dynamicProgramming(10))
print(dynamicProgramming(6))
