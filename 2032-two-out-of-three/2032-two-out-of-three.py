class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        freq = {}
        for num in set(nums1):
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in set(nums2):
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in set(nums3):
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        out = []
        for key,val in freq.items():
            if val >= 2:
                out.append(key)
        return out