class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            
        output = ""
        for ch1,ch2 in zip(word1,word2):
            output += ch1 + ch2
        
        if len(word2) > len(word1):
            output += word2[len(word1):] 
        elif len(word1) > len(word2):
            output += word1[len(word2):] 
        
        return output