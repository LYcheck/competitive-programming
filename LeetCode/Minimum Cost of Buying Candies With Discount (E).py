class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        
        res = 0
        for c in range(len(cost)):
            if c == 0 or not (c+1)%3 == 0:
                res += cost[c]
                
        return res