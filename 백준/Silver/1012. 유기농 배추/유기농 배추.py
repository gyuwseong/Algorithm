import sys
import collections

t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())  # 가로길이, 세로길이, 배추 개수
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    dfs_visited = set()
    cnt = 0


    def bfs(x, y):
        q = collections.deque([(x, y)])
        dfs_visited.add((x, y))
        while q:
            x, y = q.popleft()
            direc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dx, dy in direc:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in dfs_visited and graph[nx][ny] == 1:
                        q.append((nx, ny))
                        dfs_visited.add((nx, ny))


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and (i, j) not in dfs_visited:
                bfs(i, j)
                cnt += 1

    print(cnt)
