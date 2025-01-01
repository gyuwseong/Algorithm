import collections
import sys

n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (n + 1)
q = collections.deque([1])
while q:
    x = q.popleft()
    for i in tree[x]:
        if parents[i] == 0:
            parents[i] = x
            q.append(i)

for j in range(2, n + 1):
    print(parents[j])
