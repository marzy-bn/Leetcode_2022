class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        i = 0
        while i < len(arr)-1:
            if i == 0:
                diff = arr[i] - arr[i+1]
            else:
                if arr[i] - arr[i+1] != diff:
                    return False
                else:
                    diff = arr[i] - arr[i+1]
            i += 1
        return True