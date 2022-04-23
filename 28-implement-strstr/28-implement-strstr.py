class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i,ch in enumerate(haystack):
            if ch == needle[0]:
                if needle == haystack[i:i+len(needle)]:
                    return i
        return -1