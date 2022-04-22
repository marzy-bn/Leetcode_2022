class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        nums = []
        for word in s.split():
            if word.isnumeric():
                nums.append(int(word))
        
        i = 0
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                return False
            i += 1
        return True