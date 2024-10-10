import sys
import collections

input = sys.stdin.readline
n_list = collections.Counter(input().replace("6", "9"))

if n_list['9']:
    n_list['9'] = (n_list['9'] + 1) // 2
print(n_list.most_common()[0][1])