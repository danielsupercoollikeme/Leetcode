class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = 0
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                x = nums.index(a)
                if x == i:
                    continue
                break
        return i, x