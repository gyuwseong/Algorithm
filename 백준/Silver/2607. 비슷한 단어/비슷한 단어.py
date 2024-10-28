import sys
import collections

n = int(sys.stdin.readline().strip())
base_word = collections.Counter(list(sys.stdin.readline().strip()))
cnt = 0
for _ in range(n - 1):
    compare_word = collections.Counter(list(sys.stdin.readline().strip()))
    diff_cnt = sum((base_word - compare_word).values()) + sum((compare_word - base_word).values())
    if diff_cnt <= 2 and abs(sum(base_word.values()) - sum(compare_word.values())) <= 1:
        cnt += 1
print(cnt)