class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for letter in s:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1
        
        for i,letter in enumerate(s):
            if seen[letter] == 1:
                return i
        return -1
                