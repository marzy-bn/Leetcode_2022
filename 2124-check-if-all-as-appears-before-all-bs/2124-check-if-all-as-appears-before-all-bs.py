class Solution:
    def checkString(self, s: str) -> bool:
        flag = 0
        for ch in s:
            if flag == 0 and ch == 'b':
                flag = 1
            elif flag == 1 and ch == 'a':
                return False
        return True