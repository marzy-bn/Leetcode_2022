class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        out = 0
        p1 = 0
        while p1 < len(nums)-1:
            p2 = p1 + 1
            while p2 < len(nums):
                if nums[p1] == nums[p2]:
                    out += 1
                p2 += 1
            p1 += 1
        return out
            