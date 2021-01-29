def solution(n, k, nums):
    result = set()
    for i in range(1, n):
        for j in range(i+1, n):
            for m in range(j+1, n):
                result.add(nums[i]+nums[j]+nums[m])
    return sorted(list(result), reverse=True)[k-1]