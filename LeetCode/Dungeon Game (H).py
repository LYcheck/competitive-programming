class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        
        dp = [ [float('inf')] * (cols+1) for row in range(rows+1) ]
        dp[rows][cols-1] = 1
        dp[rows-1][cols] = 1
        
        for col in range(cols-1, -1, -1):
            for row in range(rows-1, -1, -1):
                dp[row][col] = max( min(dp[row+1][col], dp[row][col+1]) - dungeon[row][col],
                                    1)
        for row in range(rows+1):
            print(dp[row])
                
        return dp[0][0]
        
        
#         PAIN
#         dp = [ [float('inf')] * cols for i in range(rows) ]
#         dp[0][0] = dungeon[0][0]
        
#         minsofar = dp[0][0]
#         for i in range(1, cols):
#             dungeon[0][i] += dungeon[0][i-1]
#             minsofar = min(minsofar, dungeon[0][i])
#             dp[0][i] = minsofar
        
#         minsofar = dp[0][0]
#         for i in range(1, rows):
#             dungeon[i][0] += dungeon[i-1][0]
#             minsofar = min(minsofar, dungeon[i][0])
#             dp[i][0] = minsofar
        
#         for row in range(1, rows):
#             for col in range(1, cols):
#                 if dp[row-1][col] > dp[row][col-1]:
#                     dungeon[row][col] += dungeon[row-1][col]
#                     dp[row][col] = min(dungeon[row][col], dp[row-1][col])
                    
#                 elif dp[row][col-1] > dp[row-1][col]:
#                     dungeon[row][col] += dungeon[row][col-1]
#                     dp[row][col] = min(dungeon[row][col], dp[row][col-1])
#                 else:
#                     dungeon[row][col] += max(dungeon[row-1][col],
#                                             dungeon[row][col-1])
#                     dp[row][col] = min(dp[row][col], dp[row-1][col])
        
#         return -dp[rows-1][cols-1] if dp[rows-1][cols-1] < 0 else 1