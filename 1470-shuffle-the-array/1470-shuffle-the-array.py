class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p1 = 0
        p2 = n
        output = []
        while p2 < len(nums):
            output.append(nums[p1])
            p1 += 1
            output.append(nums[p2])
            p2 += 1
        return output