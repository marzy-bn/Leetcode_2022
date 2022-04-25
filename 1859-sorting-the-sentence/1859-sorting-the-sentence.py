class Solution:
    def sortSentence(self, s: str) -> str:
        hmap = {}
        output = ""
        for word in s.split():
            hmap[word[-1]] = word[:len(word)-1]
        
        for i in range(1,len(hmap)+1):
            output += hmap[str(i)] + " "
        
        return output[:len(output)-1]