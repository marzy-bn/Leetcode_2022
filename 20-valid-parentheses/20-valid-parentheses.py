class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')':'(','}':'{',']':'['}
        stack = []
        for ch in s:
            if ch in lookup.values():
                stack.append(ch)
            elif stack and lookup[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
                
                
                