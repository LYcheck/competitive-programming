class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        res = [-1]*cols
        
        def dfs(row, col, start):
            if not 0 <= row < rows or not 0 <= col < cols:
                return
            
            print("processing", row, col, "Val at", grid[row][col])
            if row == rows-1: #change
                if grid[row][col] == 1:
                    if col+1 == cols or grid[row][col+1] == -1: return
                else: 
                    if col == 0 or grid[row][col-1] == 1: return
                res[start] = col+1 if grid[row][col] == 1 else col-1
                return
            
            if grid[row][col] == 1:
                if col+1 == cols: return
                elif grid[row][col+1] == -1: return
                dfs(row+1, col+1, start)
            else:
                if col-1 < 0: return
                elif grid[row][col-1] == 1: return
                dfs(row+1, col-1, start)
                
        for i in range(cols):
            dfs(0, i, i)
            
        return res