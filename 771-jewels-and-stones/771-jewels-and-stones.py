class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        table = set()
        for jewel in jewels:
            table.add(jewel)
        print(table)
        
        count = 0
        for stone in stones:
            if stone in table:
                count += 1
        return count