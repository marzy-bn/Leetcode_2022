class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_acc = 0
        for account in accounts:
            sum_acc = 0
            for num in account:
                sum_acc += num
            if max_acc < sum_acc:
                max_acc = sum_acc
        return max_acc