class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for operation in operations:
            if operation == '--X' or operation == 'X--':
                num -= 1
            elif operation ==  '++X' or operation == 'X++':
                num += 1
        return num