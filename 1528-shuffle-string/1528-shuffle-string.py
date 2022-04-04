class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        temp = list(s)
        
        for idx,val in enumerate(s):
            temp[indices[idx]] = val
        
        return ''.join(temp)
        