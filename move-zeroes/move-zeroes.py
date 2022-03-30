class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move = 0
        left = 0
        while move < len(nums):
            if nums[move] != 0:
                temp = nums[left]
                nums[left] = nums[move]
                nums[move] = temp
                left += 1
            move += 1
                