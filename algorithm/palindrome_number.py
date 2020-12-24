class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            return int(str(x)[::-1]) == x