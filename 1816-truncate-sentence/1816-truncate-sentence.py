class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words_arr = s.split()
        return ' '.join(words_arr[:k])