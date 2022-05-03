class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        print(intervals)
        for i in range(1, len(intervals)):
            cur = intervals[i]
            prior = intervals[i-1]
            
            if cur[0] < prior[1]: return False
        
        return True