import sys

n = int(sys.stdin.readline().strip())
l = len(str(n))
cnt = 0

for i in range(l - 1):
    cnt += 9 * (i + 1) * 10 ** i
cnt += l * (n - (10 ** (l - 1)) + 1)
print(cnt)