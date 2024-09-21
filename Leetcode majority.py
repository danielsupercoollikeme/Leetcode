class Solution(object):
    def solution_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0 
        b = 0
        n = len(nums)
        for i in range(n):
            if a == 0 and b != nums[i]:
                b = nums[i]
                a += 1
            elif b == nums[i]:
                a += 1
            else:
                a -= 1
        return b
    def solution_fast(self, nums):
        for i in nums:
            if nums.count(i) > len(nums) // 2:
                return i
