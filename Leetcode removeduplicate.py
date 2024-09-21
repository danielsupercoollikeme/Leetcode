class Solution(object):
    def removeDuplicates_myself(self, nums):
        a = 0 
        b = 1
        while b in range(len(nums)):
            if nums[a] == nums[b]:
                b += 1
            else:
                nums[a + 1] = nums[b]
                b += 1
                a += 1
        return a + 1
    def solution_fast(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)
    def solution_pop(self, nums):
        i = 0 
        while i < len(nums):
            if nums[i] == nums[i] - 1:
                nums.pop(i)
            else: 
                i += 1
        return len(nums)