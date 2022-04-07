class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hmap = {}
        for i,num in enumerate(nums):
            if num not in hmap:
                hmap[num] = [i]
            else:
                hmap[num].append(i)
        print(hmap)
        
        count = 0
        for key,val in hmap.items():
            if len(val) > 1:
                count += (len(val) * (len(val) - 1) // 2 )
        return count
                
            