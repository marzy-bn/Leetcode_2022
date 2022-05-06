class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        lookup = {}
        nums_sorted = sorted(nums)
        for i,num in enumerate(nums_sorted):
            if num not in lookup:
                lookup[num] = i
        output = []
        for num in nums:
            output.append(lookup[num])
        return output
                
                
        