class Solution(object):
    def solution_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = set()
        for i in nums:
            if i in l:
                return True
            else:
                l.add(i)
    def solution_dict(self, nums):
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]):
                return True
            else:
                d[nums[i]] = True
        return False