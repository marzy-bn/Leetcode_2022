class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        i = 0
        operations = 0
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                diff = nums[i] - nums[i+1]
                operations += diff + 1
                nums[i+1] += diff + 1
            i += 1
        return operations