class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for letter in word:
            if letter.isupper():
                count += 1
        
        if count == len(word) or count == 0 or (word[0].isupper() and count == 1):
            return True
        return False

        
        '''
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
        '''