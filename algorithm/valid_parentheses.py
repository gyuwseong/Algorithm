def isValid(s) -> bool:
    left = ['(','{','[']
    right = [')','}',']']
    result = []
    for i in s:
        if i in left:
            result.append(i)
        if i in right:
            if len(result) == 0 or left.index(result.pop()) != right.index(i):
                return False
    return len(result) == 0