class Solution(object):
    def isPalindrome_myself(self, x):
        if x < 0:
            return False
        a = list(str(x))
        b = list(str(x))
        b.reverse()
        if a == b:
           return True
        return False
    def solution_slice(self, x):
        s = str(x)
        t = s[::-1]
        if s == t:
            return True
        return False
    def solution_algorithm(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        n = 0
        while x > n:
            n = n * 10 + x % 10
            x //= 10
        if x == n or x == n // 10:
            return True
        return False    