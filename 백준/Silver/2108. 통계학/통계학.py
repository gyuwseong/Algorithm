import collections
import sys

n = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for i in range(n)])


def findMin(lst):
    if len(lst) < 2:
        return lst[0]
    else:
        dic = collections.Counter(lst).most_common(2)
        return dic[1][0] if dic[0][1] == dic[1][1] else dic[0][0]


def roundUp(num):
    if num > 0:
        return int(num) + 1 if (num - int(num)) > 0.5 else int(num)
    else:
        return int(num) - 1 if (num - int(num)) < -0.5 else int(num)


print(roundUp(sum(lst) / n))
print(lst[(n - 1) // 2])
print(findMin(lst))
print(lst[-1] - lst[0])