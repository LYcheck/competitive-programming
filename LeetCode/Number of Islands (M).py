class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(grid, i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == '0':
                return 0
        
            grid[i][j] = '0'
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)

            return 1
    
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += dfs(grid, i, j)
        
        return res