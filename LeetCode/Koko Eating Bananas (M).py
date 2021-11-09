class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 10**10
        best = float('inf')
        
        while l < r:
            m = (l+r)//2
            
            total = 0
            for pile in piles:
                total += ceil(pile/m)
            
            if total <= h:
                r = m
            else:
                l = m+1
                
        return l
                