class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        
        dp = [[0] * (cols+1) for j in range(rows+1)]
            
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                up = dp[row-1][col]
                left = dp[row][col-1]
                diag = dp[row-1][col-1]
                if matrix[row-1][col-1] == "1":
                    dp[row][col] = min(up, left, diag)+1
                    res = max(res, dp[row][col])
        
        print(dp)
        return res*res