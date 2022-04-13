class Solution:
    def isMonotonic(self, nums: List[int]) -> bool: 
        decrease = True
        increase = True
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                decrease = False
            if nums[i] > nums[i+1]:
                increase = False
            i += 1
        return decrease or increase
                
                
                