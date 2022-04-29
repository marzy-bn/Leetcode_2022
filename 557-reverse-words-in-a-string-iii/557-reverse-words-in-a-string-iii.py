class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""
        for word in s.split():
            output += word[::-1] + ' '
        return output[:len(output)-1]