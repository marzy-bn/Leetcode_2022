class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        out = ""
        for ch in s:
            if ch.isalnum():
                out += ch
        
        return out[::-1] == out