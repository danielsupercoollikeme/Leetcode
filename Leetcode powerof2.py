import math
class Solution(object):

    def solution_myself(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        while n > 0:
            if n == 1:
                return True
            if n % 2 != 0:
                break
            n //= 2
        return False
    def solution_log(self, n):
        if n == 0:
            return False
        return math.floor(math.log2(n)) == math.ceil(math.log2(n))
        