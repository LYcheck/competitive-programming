class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        for i in range(1, n):
            for j in range(n):
                minsum = float('inf')
                
                for k in range(n):
                    if j == k:
                        continue
                    elif grid[i-1][k] < minsum:
                        minsum = grid[i-1][k]
                grid[i][j] += minsum
                
        
        res = float('inf')
        for _ in range(n):
            if grid[n-1][_] < res:
                res = grid[n-1][_]
                
        return res