import collections
import sys

n, m = map(int, sys.stdin.readline().split())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

result_count = float('inf')
result_nums = 0


def bfs(x):
    visited = [-1] * (n + 1)
    q = collections.deque([x])
    visited[x] = 0

    while q:
        y = q.popleft()
        for j in friends[y]:
            if visited[j] == -1:
                visited[j] = visited[y] + 1
                q.append(j)
    return sum(visited[1:])


for i in range(1, n + 1):
    counts = bfs(i)
    if result_count > counts:
        result_count = counts
        result_nums = i

print(result_nums)
