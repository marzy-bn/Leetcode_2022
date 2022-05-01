class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = -1
        for i, char in enumerate(word):
            if char == ch:
                end = i
                break
        if end != -1:
            first = word[:i+1]
            return first[::-1]  + word[i+1:]
        else:
            return word
                