class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = 0
        count = 0
        for letter in s[::-1]:
            if letter == ' ' and flag == 0:
                continue
            count += 1
            flag = 1
            if letter == ' ' and flag == 1:
                return count-1
        return count