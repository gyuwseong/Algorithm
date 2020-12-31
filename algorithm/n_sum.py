"""
1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
입력: n
출력: 1부터 n까지의 숫자를 더한 값
"""
def Sum(n):
    num = 0
    for i in range(n+1):
        num = num + i
    return num


"""
1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
입력: n
출력: 1부터 n까지의 숫자를 더한 값
"""
def Summ(n):
    return (n * (n+1)) // 2