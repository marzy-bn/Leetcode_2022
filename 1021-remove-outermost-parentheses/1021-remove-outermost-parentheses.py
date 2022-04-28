class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        c_open = 0
        c_close = 0
        rem = set()
        for i,p in enumerate(s):
            if c_open == 0 and c_close == 0:
                rem.add(i)    
            if p == '(':
                c_open += 1
            if p == ')':
                c_close += 1
            if c_open == c_close:
                c_open = 0
                c_close = 0
                rem.add(i)
        
        out = ""
        for i,ch in enumerate(s):
            if i not in rem:
                out += ch
        return out