class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            one, two = heapq.heappop(sticks), heapq.heappop(sticks)
            
            cost += one + two
            
            heapq.heappush(sticks, one+two)
            
        return cost