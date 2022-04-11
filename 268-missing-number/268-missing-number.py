class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        #[0 1 3]
        if nums[-1] < len(nums):
            return len(nums)
        idx = 0
        while idx < len(nums):
            if idx != nums[idx]:
                return idx
            idx += 1
        