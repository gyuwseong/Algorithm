import collections
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
friends = list([] for _ in range(n + 1))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited_bfs = [False] * (n + 1)
q = collections.deque([(1, 0)])
visited_bfs[1] = True
count = 0

while q:
    target, depth = q.popleft()

    if depth < 2:
        for friend in friends[target]:
            if not visited_bfs[friend]:
                q.append((friend, depth + 1))
                visited_bfs[friend] = True
                count += 1
print(count)
