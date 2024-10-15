import sys

n, k = map(int, sys.stdin.readline().split())
ipt_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
target = [lst for lst in ipt_lst if lst[0] == k][0]
sorted_lst = sorted(ipt_lst, key=lambda x: (-x[1], -x[2], -x[3]))
cnt = 1
for idx, g, s, b in sorted_lst:
    if idx == k:
        break
    elif g == target[1] and s == target[2] and b == target[3]:
        continue
    else:
        cnt += 1

print(cnt)