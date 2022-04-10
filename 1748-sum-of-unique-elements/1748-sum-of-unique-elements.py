class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        seen = []
        for num in nums:
            if num not in unique and num not in seen:
                unique.append(num)
            elif num in unique:
                unique.remove(num)
                seen.append(num)
        out = 0
        for num in unique:
            out += num
        return out