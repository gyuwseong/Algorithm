import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
st = sorted(list(set(lst)))

dic = {st[i]: i for i in range(len(st))}

for j in lst:
    print(dic[j], end=" ")