class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for segment in s.split():
            count += 1
        return count