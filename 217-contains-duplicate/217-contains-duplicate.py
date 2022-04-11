class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist = set()
        for num in nums:
            if num not in dist:
                dist.add(num)
            else:
                return True
        return False
        """
        nums.sort()
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                return True
        return False
        """