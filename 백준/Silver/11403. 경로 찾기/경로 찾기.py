import sys

n = int(sys.stdin.readline().strip())
graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for _ in graph:
    print(*_)
