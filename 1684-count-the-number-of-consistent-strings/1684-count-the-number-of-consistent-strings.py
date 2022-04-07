class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_str = set(allowed)
        out = 0
        for word in words:
            c = 1
            for letter in word:
                if letter not in set_str:
                    c = 0
                    break
            out += c
        return out
            
            
                