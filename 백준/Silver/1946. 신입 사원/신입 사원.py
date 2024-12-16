import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    people = [0] * (n + 1)
    for _ in range(n):
        s, m = map(int, sys.stdin.readline().split())
        people[s] = m

    max_value = people[1]
    count = 1

    for i in range(2, n + 1):
        if people[i] < max_value:
            max_value = people[i]
            count += 1
    print(count)
