class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        c = (n * (n + 1)) // 2
        ans = sum(nums)
        return c - ans