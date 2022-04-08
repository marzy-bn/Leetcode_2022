class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n kids with candies
        # interger array candies
        # each candies[i] = number of candies the ith kid has
        # extraCandies = number of extra candies you have
        
        output = []
        max_c = 0
        for candy in candies:
            all_c = candy + extraCandies
            if candy > max_c:
                max_c = candy
        for i,candy in enumerate(candies):
            if candy + extraCandies >= max_c:
                output.append(True)
            else:
                output.append(False)
        return output
            