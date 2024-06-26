import sys

w = sys.stdin.readline().strip().split("-")

nums = []
for i in w:
    tmp = [int(j) for j in i.split("+")]
    nums.append(sum(tmp))

rst = nums[0]

for j in range(1, len(nums)):
    rst -= nums[j]
print(rst)
