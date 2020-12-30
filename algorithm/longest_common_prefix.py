def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    shortest = min(strs, key=len)
    for i, j in enumerate(shortest):
        for word in strs:
            if word[i] != j:
                return shortest[:i]
    return shortest