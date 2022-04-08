class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i,j in zip(index,nums):
            if len(target) == i:
                target.append(j)
            else:
                target.insert(i,j)
        return target