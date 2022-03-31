class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = len(nums) - 1
        end = len(nums)
        while p1 < end:
            nums.append(nums[p1])
            p1 += 1
        return nums