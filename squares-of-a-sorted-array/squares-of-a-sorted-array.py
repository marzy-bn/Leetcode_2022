class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        i = 0
        j = len(nums)-1
        while len(out) != len(nums):
            if nums[i]**2 <= nums[j]**2:
                out.append(nums[j]**2)
                j-=1
            else:
                out.append(nums[i]**2)
                i+=1
        return out[::-1]