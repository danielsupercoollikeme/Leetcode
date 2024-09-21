class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = []
        while n != 1:
            if n in l:
                return False
            l.append(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True
    def isHappy(self, n):
        l = []
        while n > 0:
            c = 0
            while n > 0:
                k = n % 10

                c += k * k
                n = n // 10
            if c in l:
                return False
            else:
                l.append(c)
            if c == 1:
                return True
            n = c
        return False
        