class Solution:
    def maxScore(self, s: str) -> int:
        
        i = 0
        num0 = 0
        hmap0 = {}
        while i < len(s):
            if s[i] == '0':
                num0 += 1
            hmap0[i] = num0
            i += 1
        print(hmap0)
        
        j = len(s) - 1
        num1 = 0
        hmap1 = {}
        while j >= 0:
            if s[j] == '1':
                num1 += 1
            hmap1[j] = num1
            j -= 1
        print(hmap1)
        
        max_val = 0
        for i in range(len(s)-1):
            val = hmap0[i] + hmap1[i+1]
            if val >= max_val:
                max_val = val
        return max_val
                
        
        