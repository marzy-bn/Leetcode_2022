class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
        for idx,num in enumerate(nums):
            if num == target:
                output.append(idx) 
        return output