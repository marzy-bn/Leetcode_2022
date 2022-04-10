class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        alts = [0]
        i = 0
        for num in gain:
            alts.append(alts[i] + num)
            i += 1
            if max_alt < alts[i]:
                max_alt = alts[i]
        return max_alt