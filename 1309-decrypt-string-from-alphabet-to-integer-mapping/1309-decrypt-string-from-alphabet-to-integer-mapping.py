class Solution:
    def freqAlphabets(self, s: str) -> str:
        hmap1 = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
        hmap2 = {'10#':'j','11#':'k','12#':'l','13#':'m','14#':'n','15#':'o','16#':'p','17#':'q','18#':'r',
                 '19#':'s','20#':'t','21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        
        output = ''
        
        i = len(s)-1
        while i >= 0:
            if s[i] == '#':
                output += hmap2[s[i-2:i+1]]
                i -= 3
            else:
                output += hmap1[s[i]]
                i -= 1
        
        return output[::-1] 