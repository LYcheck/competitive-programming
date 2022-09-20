class Solution:
    def solve(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * (cols+1) for j in range(rows+1)]
            
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                if matrix[row-1][col-1] == 1:
                    dp[row][col] =  min(dp[row-1][col], \
                                        dp[row][col-1], \
                                        dp[row-1][col-1])+1

                    res = max(res, dp[row][col]*dp[row][col])
        
        return res