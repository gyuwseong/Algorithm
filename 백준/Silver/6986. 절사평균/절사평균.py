import sys

n, k = map(int, sys.stdin.readline().split())
input_list = sorted(list(float(sys.stdin.readline().strip()) for _ in range(n)))
s_score = sum(input_list[k:n - k]) / (n - 2 * k)
b_score = (sum(input_list[k:n - k]) + input_list[k] * k + input_list[n - k - 1] * k) / n

print("{:.2f}".format(s_score + 1e-8))
print("{:.2f}".format(b_score + 1e-8))