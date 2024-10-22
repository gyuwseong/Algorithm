import sys

n = int(sys.stdin.readline().strip())
dic = {}
for _ in range(n):
    ipt = sys.stdin.readline().strip()
    if ipt in dic:
        dic[ipt] += 1
    else:
        dic[ipt] = 1

sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dic[0][0])