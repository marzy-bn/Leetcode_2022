class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = ''
        other = {}
        for i,char in enumerate(s):
            if char.isalpha() == True:
                alpha += char
            else:
                other[i] = char
        alpha = alpha[::-1]
        
        output = ""
        
        i = 0
        j = 0
        while i < len(s):
            if i not in other.keys():
                output += alpha[j]
                j += 1
            else:
                output += other[i]
            i+=1
        
        return output
            