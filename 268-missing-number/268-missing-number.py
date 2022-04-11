class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hset = set()
        for idx in range(len(nums)+1):
            hset.add(idx)
        print(hset)
        idx = 0
        while idx < len(nums):
            if nums[idx] in hset:
                hset.remove(nums[idx])
            idx += 1
        return list(hset)[0]
            