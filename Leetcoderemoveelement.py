class Solution(object):
    def removeElement_myself(self, nums, val):
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k    
    def solution_count(self, nums, val):
        k = nums.count(val)
        for i in range(k)
            nums.remove(val)
        return len(nums)
        