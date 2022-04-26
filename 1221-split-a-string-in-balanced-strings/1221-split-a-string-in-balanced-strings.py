class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        output = 0
        for i,ch in enumerate(s):
            if ch == 'R':
                count += 1
            elif ch == 'L':
                count -= 1
            if count == 0:
                output += 1
        return output
            
            