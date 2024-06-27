import sys

n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
for i in lst:
    if cnt + 1 < i:
        break
    cnt += i
print(cnt + 1)