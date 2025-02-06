import collections
import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

rst = []
visited = set()


def bfs(a, b):
    count = 1
    q = collections.deque([(a, b)])
    visited.add((a, b))

    while q:
        x, y = q.popleft()
        direcs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dx, dy in direcs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                count += 1

    return count


for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and (i, j) not in visited:
            rst.append(bfs(i, j))

if len(rst) == 0:
    print(len(rst))
    print(0)
else:
    print(len(rst))
    print(max(rst))