class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        def shift(grid):
            mem = 'x'
            for row in range(rows):
                for col in range(cols):
                    grid[row][col], mem = mem, grid[row][col]
                    
            grid[0][0] = mem
            
        for i in range(k):
             shift(grid)
                
        return grid
                    