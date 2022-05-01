class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'x' * 1
        
        if n % 2 == 0:
            m = n - 1
            return 'x' * m + 'y' * 1 
        else:
            m = n - 2
            return 'x' * m + 'y' * 1 + 'z' * 1
        
        