class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        
        for i in range(len(students)):
            res += abs(students[i]-seats[i])
        return res