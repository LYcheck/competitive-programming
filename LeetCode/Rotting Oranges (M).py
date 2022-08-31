class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        
        res = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            cur = q[0]
            q.pop(0)
            row, col, time = cur
            res = max(res, time)
            
            for drow, dcol in dirs:
                nrow = row+drow
                ncol = col+dcol
                if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 1:
                    q.append((nrow, ncol, time+1))
                    grid[nrow][ncol] = 2
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return res