class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1 = ""
        st2 = ""
        for ele in word1:
            st1 += ele
        for ele in word2:
            st2 += ele
        return st1 == st2