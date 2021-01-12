def same_name(names):
    result = set()
    for i in range(len(names)-1):
        for j in range(i+1,len(names)):
            if names[i] == names[j]:
                result.add(names[i])
    return result