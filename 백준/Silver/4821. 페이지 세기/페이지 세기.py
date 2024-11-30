import sys

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break

    page_list = list(sys.stdin.readline().strip().split(","))
    pages = set()
    for p in page_list:
        if "-" in p:
            low, high = map(int, p.split("-"))
            if low > high or low > n:
                continue
            for i in range(low, high + 1 if high < n else n + 1):
                pages.add(i)
        else:
            if int(p) <= n:
                pages.add(int(p))
    print(len(pages))
