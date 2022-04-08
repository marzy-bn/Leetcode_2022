class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i,j in zip(index,nums):              
            target.insert(i,j)
        return target