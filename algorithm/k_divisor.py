# 풀이 1
def solution1(n, k):
    result = []
    for i in range(1,k+1):
        if n % i == 0:
            result.append(i)
    return -1 if len(result) < k else result[i-1]


# 풀이 2
def solution2(n, k):
    count = 0
    for i in range(1,k+1):
        if n % i == 0:
            count += 1
        if count == k:
            return i
    else:
        return -1