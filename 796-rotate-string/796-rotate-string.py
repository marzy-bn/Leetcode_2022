class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        output = ""
        i = 0
        while i < len(s):
            output = s[i+1:] + s[:i+1]
            if goal == output:
                return True
            i += 1
        return False
        