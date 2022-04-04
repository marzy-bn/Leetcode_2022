class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        htable = {}
        
        i = 0
        while i < len(s):
            htable[indices[i]] = s[i]
            i += 1
        
        arr = list(s)
        
        for key in htable:
            arr[key] = htable[key]
        
        out = ""
        return out.join(arr)