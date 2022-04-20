class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        occr1 = set()
        seen1 = set()
        
        for word in words1:
            if word not in occr1 and word not in seen1:
                occr1.add(word)
            elif word in occr1 and word not in seen1:
                occr1.remove(word)
                seen1.add(word)
        print(occr1)
        print(seen1)
        
        occr2 = set()
        seen2 = set()
        
        for word in words2:
            if word not in occr2 and word not in seen2:
                occr2.add(word)
            elif word in occr2 and word not in seen2:
                occr2.remove(word)
                seen2.add(word)
        print(occr2)
        print(seen2)
        
        c = 0
        for word1 in occr1:
            if word1 in occr2:
                c += 1
        
        return c