import sys

n, m = map(int, sys.stdin.readline().split())
input_list = list(map(int, sys.stdin.readline().split()))

count = 0
sums = 0
start = 0

for i in range(n):
    sums += input_list[i]

    while sums > m:
        sums -= input_list[start]
        start += 1

    if sums == m:
        count += 1

print(count)
