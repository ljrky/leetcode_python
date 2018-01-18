def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    if not s:
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and (not str(s[left]).isalnum()):
            left = left + 1
        while left < right and (not str(s[right]).isalnum()):
            right = right - 1
        if s[left].lower() != s[right].lower():
            return False
        else:
            left = left + 1
            right = right - 1

    return True

test = "ab"
result = isPalindrome(test)
print(result)