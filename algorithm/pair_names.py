def pair_names(names):
    result = []
    for i in range(len(names)-1):
        for j in range(i,len(names)):
            if names[i] != names[j]:
                result.append(names[i] + "-" + names[j])
    return result