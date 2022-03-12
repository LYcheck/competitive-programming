class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols:
                if grid[row][col]: return True
                else:
                    grid[row][col] = 1
                    inres = True
                    for dx, dy in directions:
                        inres &= dfs(row+dy, col+dx)
                    
                    return inres
                
            return False
        
        for erow in range(rows):
            for ecol in range(cols):
                if not grid[erow][ecol]: 
                    if dfs(erow, ecol): res += 1
                    
                    
        return res