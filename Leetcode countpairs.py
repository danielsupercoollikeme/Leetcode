class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            k = nums[i]
            for j in range(i + 1, len(nums)):
                if (k + nums[j]) < target:
                    c += 1
        return c
            
                
        