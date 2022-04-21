class Solution:
    def maxPower(self, s: str) -> int:
        out = 0
        count = 1
        i = 0
        while i < len(s)-1:
            if s[i] == s[i+1]:
                count += 1
            else:
                if count >= out:
                    out = count
                count = 1
            i += 1
        
        if count > out:
            return count
        
        return out