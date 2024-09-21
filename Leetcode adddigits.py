class Solution(object):
    def solution_myself(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
    def solution_while(self, num):
        while num > 9:
            num = num % 10 + num // 10
        return num
        