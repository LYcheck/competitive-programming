class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        old = image[sr][sc]
        if newColor == old: return image
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        
        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and image[row][col] == old:
                image[row][col] = newColor
                for dx, dy in dirs:
                    dfs(row+dx, col+dy)
            else:
                return
            
        dfs(sr, sc)
        
        return image