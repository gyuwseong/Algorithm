import sys

n, k = map(int, sys.stdin.readline().split())
tem_list = list(map(int, sys.stdin.readline().split()))

current_sums = sum(tem_list[:k])
max_sums = current_sums

for i in range(k, n):
    current_sums += tem_list[i] - tem_list[i - k]
    max_sums = max(max_sums, current_sums)
print(max_sums)