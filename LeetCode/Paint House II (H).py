class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        min1, min2 = -1, -1
        
        for i in range(n):
            lmin1, lmin2 = min1, min2
            min1, min2 = -1, -1
            for j in range(k):
                if j != lmin1:
                    costs[i][j] += costs[i-1][lmin1] if lmin1 >= 0 else 0
                else:
                    costs[i][j] += costs[i-1][lmin2] if lmin2 >= 0 else 0
                    
                if min1 == -1 or costs[i][j] < costs[i][min1]:
                    min1, min2 = j, min1
                elif min2 == -1 or costs[i][j] < costs[i][min2]:
                    min2 = j
        
        return costs[n-1][min1]