import sys

dic = {}
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    dic[tree] = dic.get(tree, 0) + 1

sorted_dic = dict(sorted(dic.items()))
sums = sum(dic.values())

for k, v in sorted_dic.items():
    print("%s %.4f" % (k, (v / sums) * 100))
