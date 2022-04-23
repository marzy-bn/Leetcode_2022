class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        if len(strs) == 0:
            return prefix
        
        for letter in strs[0]:
            prefix += letter

        for st in strs[1:]:
            if len(st) < len(prefix):
                prefix = prefix[:len(st)]
            i = 0
            while i < len(prefix):
                if prefix[i] != st[i]:
                    prefix = prefix[:i]
                i += 1
        return prefix
        
        
        