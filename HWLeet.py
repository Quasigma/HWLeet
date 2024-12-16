def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

strs1 = ["flower", "flow", "flight"]
print("Первая строка: ", longestCommonPrefix(strs1))

strs2 = ["dog", "racecar", "car"]
print("Вторая строка: ", longestCommonPrefix(strs2))
