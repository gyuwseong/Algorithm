import sys
import collections

n = int(sys.stdin.readline().strip())
info_dic = collections.defaultdict(int)

for _ in range(n):
    name, info = sys.stdin.readline().strip().split(".")
    info_dic[info] += 1

for key, value in sorted(info_dic.items()):
    print(f"{key} {value}")