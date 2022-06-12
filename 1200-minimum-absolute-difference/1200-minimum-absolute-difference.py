class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        results = []
        mini = 1000000000
        
        arr.sort()
        for a,b in zip(arr,arr[1:]):
            diff = abs(a-b)
            if diff == mini:
                results.append([a,b])
                #print("ppp",results)
            elif diff < mini:
                mini = diff
                results = [(a,b)]
                #print("sss",results)
        return results
                