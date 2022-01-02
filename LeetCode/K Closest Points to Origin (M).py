class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            mag = x*x + y*y
            
            heapq.heappush(heap, (-mag, x, y))
            
            if len(heap) > k:
                heapq.heappop(heap)
            
                
        res = []
        
        while heap:
            resr = heapq.heappop(heap)
            res.append([resr[1], resr[2]])
            
        return res