class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [ [0]*n for i in range(2) ] 
        redbot = [ [x for x in row] for row in grid]
        
        for i in grid:
            print(i)
        
        minmax = float('inf')
        up, down = 0, 0
        idx = 0
        
        for i in range(1, n):
            redbot[0][i] += redbot[0][i-1]
            redbot[1][i] += redbot[1][i-1]
        
        for i in range(n):
            if i == n-1:
                up = redbot[0][n-1] + redbot[1][n-1]- redbot[1][n-2]
                down = redbot[0][n-1] - redbot[0][0]
            elif i == 0:
                up = redbot[1][n-1] + redbot[0][0]
                down = redbot[1][n-2]
            else:
                up = redbot[0][i] + (redbot[1][n-1] - redbot[1][i-1])
                down = max(redbot[1][i-1], redbot[0][n-1] - redbot[0][i])
            
            if down < minmax:
                minmax = down
                idx = i
                
        return minmax
                
#         for i in range(n):
#             if i == idx:
#                 grid[0][i] = 0
#                 grid[1][i] = 0
#             elif i < idx:
#                 grid[0][i] = 0
#             else:
#                 grid[1][i] = 0
    
    
#         for i in range(2):
#             for j in range(n):
#                 if j > 0 and i > 0:
#                     dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
#                 elif j > 0:
#                     dp[i][j] = grid[i][j] + dp[i][j-1]
#                 else:
#                     dp[i][j] = grid[i][j] + dp[i-1][j]
            
#         for i in grid:
#             print(i)
            
#         for i in dp:
#             print(i)
                
        return dp[1][n-1]