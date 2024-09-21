class Solution(object):
    def solution_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for key, val in d.items():
            if val == 1:
                return key
    def solution_bit(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res