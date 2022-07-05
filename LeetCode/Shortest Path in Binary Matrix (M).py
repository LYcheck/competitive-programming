class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        rows = len(grid)
        cols = len(grid[0])
        q = [(0, 0, 1)]
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        while q:
            cr, cc, cd = q[0]
            q.pop(0)
            grid[cr][cc] = 1
            
            if cr == rows-1 and cc == cols-1: return cd
            
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and not grid[nr][nc]:
                    grid[nr][nc] = 1
                    q += [(nr, nc, cd+1)]
                    
        return -1