class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hset = set()
        for i in range(1,len(nums)+1):
            hset.add(i)
        for i in nums:
            if i in hset:
                hset.remove(i)
        return list(hset)