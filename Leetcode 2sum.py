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
    def solution_bruteforce(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return[i, j]
    def solution_dictionary(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i
