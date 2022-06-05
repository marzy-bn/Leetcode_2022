class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students = 0
        for i,j in zip(startTime,endTime):
            if queryTime >= i and queryTime <= j:
                students += 1
        return students