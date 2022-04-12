class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #4 1 2 1 2
        
        xor = 0
        for num in nums:
            xor ^= num
        return xor
        