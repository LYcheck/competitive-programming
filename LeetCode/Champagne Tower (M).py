class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [ [0]*100 for i in range(100) ]
        
        dp[0][0] = poured
        
        def recurse(row):
            if row > query_row: return
            
            for j in range(row+1):
                if dp[row][j] > 1:
                    if row+1 < 100:
                        dp[row+1][j] += (dp[row][j]-1)/2
                        dp[row+1][j+1] += (dp[row][j]-1)/2
                            
                    dp[row][j] -= (dp[row][j]-1)

            recurse(row+1)
        
        recurse(0)
        print(dp)
        return dp[query_row][query_glass]