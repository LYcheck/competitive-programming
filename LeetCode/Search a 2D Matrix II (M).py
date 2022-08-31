class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols-1
        
        while 0 <= col and rows > row:
            if matrix[row][col] < target: row += 1
            elif matrix[row][col] > target: col -= 1
            else: return True
            
        return False