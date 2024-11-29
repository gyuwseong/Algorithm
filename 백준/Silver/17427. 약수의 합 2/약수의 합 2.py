import sys

n = int(sys.stdin.readline().strip())
sums = 0

for i in range(1, n + 1):
    count = n // i
    sums += i * count

print(sums)