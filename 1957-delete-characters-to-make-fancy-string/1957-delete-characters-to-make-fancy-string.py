class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""
        if len(s) <= 2:
            return s
        output += s[0] + s[1]
        for x,y,z in zip(s,s[1:],s[2:]):
            if not (x == y and y == z):
                output += z
        return output
                
            