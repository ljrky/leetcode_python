def validParenthese(s):
    leftChar = '({['
    map={
        ')':'(',
        '}':'{',
        ']':'['
    }

    stack = []

    for i in s:
        if i in leftChar:
            stack.append(i)
        else:
            if not stack or stack.pop()!=map[i]:
                return False

    if not stack:
        return True
    else:
        return False

test = '()[]{}'
test = '(]'
test = '()'
print(validParenthese(test))
