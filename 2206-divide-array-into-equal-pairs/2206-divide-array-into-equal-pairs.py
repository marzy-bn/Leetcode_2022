class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pair_dict = {}
        for num in nums:
            if num not in pair_dict:
                pair_dict[num] = 1
            else:
                pair_dict[num] += 1
        for val in pair_dict.values():
            if val % 2 != 0:
                return False
        return True