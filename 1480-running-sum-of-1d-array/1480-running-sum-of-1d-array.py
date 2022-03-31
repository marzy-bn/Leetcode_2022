class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        idx = 0
        sumall = 0
        while idx < len(nums):
            nums[idx] = sumall + nums[idx]
            sumall = nums[idx]
            idx += 1
        return nums