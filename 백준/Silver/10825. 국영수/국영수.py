import sys

n = int(sys.stdin.readline().strip())
score_dic = {}

for _ in range(n):
    name, a, b, c = sys.stdin.readline().split()
    score_dic[name] = [int(a), int(b), int(c)]

sorted_dic = dict(sorted(score_dic.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0])))
for _ in sorted_dic.keys():
    print(_)