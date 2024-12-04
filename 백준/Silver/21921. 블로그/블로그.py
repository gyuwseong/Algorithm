import sys

n, x = map(int, sys.stdin.readline().split())
visit_list = list(map(int, sys.stdin.readline().split()))

max_sums = sum(visit_list[:x])
current_sums = max_sums
count = 1

for i in range(x, n):
    current_sums += visit_list[i] - visit_list[i - x]
    if max_sums == current_sums:
        count += 1
    elif current_sums > max_sums:
        max_sums = current_sums
        count = 1

if max_sums == 0:
    print("SAD")
else:
    print(max_sums)
    print(count)
