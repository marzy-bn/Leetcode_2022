class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        word_max = 0
        for sentence in sentences:
            word_count = 0
            for i,letter in enumerate(sentence):
                if letter == ' ':
                    word_count += 1
            if word_count + 1 > word_max:
                word_max = word_count + 1
        return word_max
        
                    
            
            