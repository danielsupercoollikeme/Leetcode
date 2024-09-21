class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        c = 0
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    c += 1
            l.append(c)
        return l
        