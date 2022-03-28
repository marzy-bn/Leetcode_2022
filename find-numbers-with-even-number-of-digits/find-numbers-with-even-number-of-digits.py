class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evencount = 0
        for num in nums:
            temp = num
            count = 0
            while temp // 10 != 0:
                count += 1
                temp = temp // 10
            count += 1
            if count % 2 == 0:
                evencount += 1
        return evencount