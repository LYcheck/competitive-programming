class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] = min(matrix[i][j] + matrix[i-1][j], matrix[i][j] + matrix[i-1][j+1])
                elif j == n-1:
                    matrix[i][j] = min(matrix[i][j] + matrix[i-1][j], matrix[i][j] + matrix[i-1][j-1])
                else:
                    matrix[i][j] = min(matrix[i][j] + matrix[i-1][j], matrix[i][j] + matrix[i-1][j-1], matrix[i][j] + matrix[i-1][j+1])
                    
        cur = float('inf')        
        for i in range(n):
            if matrix[n-1][i] < cur:
                cur = matrix[n-1][i]
                
        return cur