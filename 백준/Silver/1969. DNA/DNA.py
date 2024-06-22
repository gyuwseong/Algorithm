import collections
import sys

n, m = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for i in range(n)]
lst = []
w_lst = []
for j in range(m):
    for i in range(len(words)):
        lst.append(words[i][j])
    commons = collections.Counter(lst).most_common()
    sorted_lst = sorted(commons, key=lambda x: (-x[1], x[0]))
    w_lst.append(sorted_lst[0][0])
    lst = []

cnt = 0
for w in words:
    for k in range(len(w)):
        if w_lst[k] != w[k]:
            cnt += 1
print("".join(w_lst))
print(cnt)