import collections
import sys

n = int(sys.stdin.readline().strip())
r = int(sys.stdin.readline().strip())
students = list(map(int, sys.stdin.readline().split()))
dic = {}

for num in students:
    if num in dic:
        dic[num] += 1
    else:
        if len(dic) < n:
            dic[num] = 1
        else:
            min_value = min(dic.values())
            target = collections.OrderedDict((k, v) for k, v in dic.items() if v == min_value)
            del dic[target.popitem(last=False)[0]]
            dic[num] = 1
print(*sorted(dic))
