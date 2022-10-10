class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def calc(row, col):
            temp = 0
            for i in range(3):
                temp += grid[row][col+i]
                temp += grid[row+2][col+i]
            temp += grid[row+1][col+1]
            return temp
        
        maxso = -float('inf')
        rows, cols = len(grid), len(grid[0])
        for i in range(rows-2):
            for j in range(cols-2):
                maxso = max(maxso, calc(i,j))
                
        return maxso