class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash_map = set()
        for num in nums:
            if num not in hash_map:
                hash_map.add(num)
            else:
                return num