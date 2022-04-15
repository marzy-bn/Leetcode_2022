class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() == True:
            return True
        if word.islower() == True:
            return True
        
        if word[0].isupper():
            i = 1
            while i < len(word):
                if word[i].isupper():
                    return False
                i += 1
        else:
            return False
        return True