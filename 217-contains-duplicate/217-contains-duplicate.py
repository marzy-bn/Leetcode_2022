class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist = set()
        for num in nums:
            if num not in dist:
                dist.add(num)
            else:
                return True
        return False