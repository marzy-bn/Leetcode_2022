class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = set()
        for num in nums:
            if num not in hmap:
                hmap.add(num)
            else:
                hmap.remove(num)
        
        return list(hmap)[-1]
        
        
        '''
        nums.sort()
        #1,1,2,2,4
        i = 0
        while i < len(nums):
            if i == len(nums)-1:
                return nums[i]
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        '''