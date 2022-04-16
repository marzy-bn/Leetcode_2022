class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        out = []
        i = 0
        for l1 in s:
            if l1 not in lookup:
                lookup[l1] = i
                i += 1
            out.append(lookup[l1])
        
        lookup2 = {}
        i = 0
        out2 = []
        for l2 in t:
            if l2 not in lookup2:
                lookup2[l2] = i
                i += 1
            out2.append(lookup2[l2])
        return out == out2
            