import collections
import sys

n, d, k, c = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().strip()) for _ in range(n))

lst.extend(lst[:k - 1])
table = collections.deque()
dic = collections.defaultdict(int)
dic[c] += 1

for i in range(k):
    table.append(lst[i])
    dic[lst[i]] += 1
max_value = len(dic)

for i in range(k, n + k - 1):
    start = table.popleft()
    dic[start] -= 1
    if dic[start] == 0:
        del dic[start]
    table.append(lst[i])
    dic[lst[i]] += 1
    max_value = max(max_value, len(dic))
print(max_value)
