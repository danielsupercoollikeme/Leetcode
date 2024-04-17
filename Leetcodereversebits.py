class Solution:
    # @param n, an integer
    # @return an integer
    def solution_myself(self, n):
        n = int(str(n)[::-1])
        decimal = 0
        i = 0
        while n != 0:
            dec = n % 10
            decimal = decimal + dec * pow(2, i)
            n = n // 10
            i += 1
        return decimal
    
#The code above should've worked but leetcode outputs the wrong output for some reason.
#Below is a correct solution

    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res