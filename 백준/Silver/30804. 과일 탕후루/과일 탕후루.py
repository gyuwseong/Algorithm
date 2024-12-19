import collections
import sys

n = int(sys.stdin.readline().strip())
fruits = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
fruits_count = collections.defaultdict(int)
max_len = 0

while end < n:
    fruits_count[fruits[end]] += 1

    while len(fruits_count) > 2:
        fruits_count[fruits[start]] -= 1
        if fruits_count[fruits[start]] == 0:
            del fruits_count[fruits[start]]
        start += 1

    max_len = max(end - start + 1, max_len)
    end += 1

print(max_len)
