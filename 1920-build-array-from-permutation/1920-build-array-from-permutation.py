class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i,val in enumerate(nums):
            ans.append(nums[val])
        return ans