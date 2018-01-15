def reverseString(s):
    if not s:
        return ''
    if s == ' ' or s == "    ":
        return ''
    if len(s) == 1:
        return s

    result = s.strip(' ').split(' ')
    if len(result) <= 1:
        return result
    else :
        return result.reverse()

test = "   a   b "
result = reverseString(test)
print(result)