class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        out1 = ""
        out2 = ""
        
        for val in s:
            if val != '#':
                out1 += val
            else:
                out1 = out1[:-1]
        for val in t:
            if val != '#':
                out2 += val
            else:
                out2 = out2[:-1]
        
        return out1 == out2
                