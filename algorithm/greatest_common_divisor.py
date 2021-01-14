def divisor(a,b):
    num = divisor(a,b)
    while True:
        if a % num == 0 and b % num == 0:
            return num
        num -= 1