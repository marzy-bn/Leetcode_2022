class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        out = ""
        for ch in s:
            if ch.isalnum():
                out += ch
        p1 = 0
        p2 = len(out)-1
        while p1 < len(out)//2:
            if out[p1] != out[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
        
        