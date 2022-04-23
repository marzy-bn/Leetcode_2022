class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        convert = ""
        for ch in word:
            if ch.isnumeric() == False:
                convert += " "
            else:
                convert += ch
        nums = set()
        for seg in convert.split():
            nums.add(int(seg))
        
        return len(nums)