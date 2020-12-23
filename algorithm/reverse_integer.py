class Solution:
    def reverse(self, x):
        if x >= 0:
            num =  int(str(x)[::-1])
            return num if num.bit_length() < 32 else 0
        elif x < 0:
            num = int(str(x).replace("-","")[::-1])
            return f"-{num}" if num.bit_length() < 32 else 0