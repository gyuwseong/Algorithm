nums = set(range(1, 10001))
sums = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    sums.add(i)

for _ in sorted(nums - sums):
    print(_)