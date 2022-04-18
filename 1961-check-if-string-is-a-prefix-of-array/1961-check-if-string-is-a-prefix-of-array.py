class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        build = ""
        for word in words:
            build += word
            if build == s:
                return True
        return False
                