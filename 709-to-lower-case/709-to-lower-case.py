class Solution:
    def toLowerCase(self, s: str) -> str:
        
        return s.lower()
        
        '''
        arr = list(s)
        
        for idx,letter in enumerate(arr):
            arr[idx] = letter.lower()
        
        out = ""
        return out.join(arr)
        '''