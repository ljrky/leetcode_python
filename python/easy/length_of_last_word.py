def lengthOfLastWord(s):
    result = s.rstrip(' ').split(' ')[-1]
    return len(result)

test = ' asdf adsdf '
result = lengthOfLastWord(test)
print(result)