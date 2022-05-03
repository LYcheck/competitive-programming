class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        heap = []
        res = 1
        
        for interval in intervals:
            s, e = interval
            
            while heap and s >= heap[0]: heapq.heappop(heap)
            heapq.heappush(heap, e)
            
            res = max(res, len(heap))
            
        return res