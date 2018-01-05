def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''

    compare_string = strs[0]

    for str in strs[1:]:
        i = 0
        while i < len(compare_string) and i < len(str) and compare_string[i] == str[i]:
            i = i + 1
        compare_string = compare_string[:i]

    return compare_string

test = ['aaa','ab']
test = ['aaa']
print(longestCommonPrefix(test))
