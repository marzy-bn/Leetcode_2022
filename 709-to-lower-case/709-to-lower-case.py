class Solution:
    def toLowerCase(self, s: str) -> str:
        
        arr = list(s)
        for idx,letter in enumerate(arr):
            arr[idx] = letter.lower()
        out = ""
        for letter in arr:
            out += letter
        return out