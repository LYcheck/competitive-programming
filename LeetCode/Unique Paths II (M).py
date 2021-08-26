class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] or obstacleGrid[h-1][w-1]:
            return 0
        
        dp = [ [0]*w for _ in range(h) ]
        dp[0][0] = 1
        
        
        for i in range(1, h):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for i in range(1, w):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
            
        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] == 1 or (obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1):
                    continue
                    
                if(obstacleGrid[i-1][j] == 1):
                    dp[i][j] = dp[i][j-1]
                elif(obstacleGrid[i][j-1] == 1):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        
        return dp[h-1][w-1]