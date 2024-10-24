import sys
import collections

n, m = map(int, sys.stdin.readline().split())
word_lst = []

for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) >= m:
        word_lst.append(word)

dic_lst = list(collections.Counter(word_lst).items())
dic_lst.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for w, _ in dic_lst:
    print(w)