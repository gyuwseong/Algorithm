import sys
import collections

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

bfs_visited = set()
dic = {}


def bfs(a, b):
    q = collections.deque([(a, b)])
    bfs_visited.add((a, b))
    cnt = 1

    while q:
        x, y = q.popleft()
        direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in direcs:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in bfs_visited and graph[nx][ny] == 1:
                q.append((nx, ny))
                bfs_visited.add((nx, ny))
                cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if (i, j) not in bfs_visited and graph[i][j] == 1:
            dic[(i, j)] = bfs(i, j)

print(len(dic))
for _ in sorted(dic.values()):
    print(_)
