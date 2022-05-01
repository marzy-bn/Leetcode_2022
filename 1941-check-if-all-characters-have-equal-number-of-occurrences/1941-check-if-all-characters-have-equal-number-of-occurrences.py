class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occur = {}
        for char in s:
            if char not in occur:
                occur[char] = 1
            else:
                occur[char] += 1
        temp = list(occur.values())[0]
        for num in occur.values():
            if num != temp:
                return False
        return True
            