import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}

    for _ in range(n):
        name, cloth_type = sys.stdin.readline().split()
        if cloth_type in dic:
            dic[cloth_type] += 1
        else:
            dic[cloth_type] = 1

    cnt = 1
    for i in dic.values():
        cnt *= i + 1

    print(cnt - 1)