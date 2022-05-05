class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ""
        for i,char in enumerate(s):
            if i == 0:
                output += char
                continue
            if i == len(s)-1:
                output += char
                break
            prior = s[i-1]
            after = s[i+1]
            if prior == char and char == after:
                continue
            else:
                output += char
        return output
                
            