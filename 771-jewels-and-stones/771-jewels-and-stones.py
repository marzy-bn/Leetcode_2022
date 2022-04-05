class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        arr = list(jewels)
        count = 0
        for stone in stones:
            if stone in arr:
                count += 1
        return count