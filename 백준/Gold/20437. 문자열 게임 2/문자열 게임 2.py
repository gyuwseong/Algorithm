import collections
import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    lst = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    lst_dic = collections.defaultdict(list)

    for i, c in enumerate(lst):
        lst_dic[c].append(i)

    min_value = float('inf')
    max_value = 0

    for count in lst_dic.values():
        if len(count) < k:
            continue

        for i in range(len(count) - k + 1):
            lst_count = count[i + k - 1] - count[i] + 1
            min_value = min(min_value, lst_count)
            max_value = max(max_value, lst_count)

    if min_value == float('inf'):
        print(-1)
    else:
        print(min_value, max_value)
