class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        mid = (len(s)//2)
        
        c1 = 0
        c2 = 0
        
        for ch in s[:mid]:
            if ch in vowels:
                c1 += 1
        
        for ch in s[mid:]:
            if ch in vowels:
                c2 += 1
        
        return c1 == c2