import sys
import collections

n, c = map(int, sys.stdin.readline().split())
input_list = list(map(int, sys.stdin.readline().split()))
input_dic = sorted(collections.Counter(input_list).items(), key=lambda x: -x[1])
result = ""
for key, value in input_dic:
    result += (str(key) + " ") * value
print(result)
