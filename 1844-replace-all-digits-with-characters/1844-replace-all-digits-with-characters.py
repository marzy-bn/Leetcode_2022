class Solution:
    def replaceDigits(self, s: str) -> str:
        
        i = 0
        j = 1
        out = ''
        while i < len(s) or j < len(s):
            out += s[i]
            if i == len(s)-1:
                break
            out += chr(ord(s[i]) + int(s[j]))
            i += 2
            j += 2
        return out