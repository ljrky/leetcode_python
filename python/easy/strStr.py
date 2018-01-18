def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) + 1):
        for j in range(len(needle) + 1):
            if j == len(needle):
                return i
            if i + j == len(haystack):
                return -1
            if haystack[i + j] != needle[j]:
                break

test = "aaaaa"
test2 = "bba"
result = strStr(test,test2)
print(result)