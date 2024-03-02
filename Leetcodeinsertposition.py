class Solution(object):
    def solution_myself(self, nums, target):
        a = 0
        c = len(nums) - 1
        while a <= c:
            b = (a + c) // 2
            if nums[b] == target:
                return b
            elif nums[b] > target:
                c = b - 1
            else: 
                a = b + 1
        return c + 1
    def solution_dictionary(self, nums, target):
        n = {}
        s = 0
        min, max = min(nums), max(nums)
        for i in nums:
            n[i] = n.get(i, 0) + 1
        for i in range(min, max + 1):
            while n.get(i, 0) > 0:
                nums[s] = i
                s += 1
                n[i] -= 1
        return nums
        