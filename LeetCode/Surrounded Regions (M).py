class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = len(board[0])
        rows = len(board)
        
        def traverse(i, j):
            if not (0 <= j < cols and 0 <= i < rows):
                return
            
            if board[i][j] == 'O': board[i][j] = 'T'
            else: return
            
            traverse(i+1, j)
            traverse(i-1, j)
            traverse(i, j+1)
            traverse(i, j-1)
                
            return
        
        for row in range(rows):
            if board[row][0] == 'O':
                traverse(row, 0)
            if board[row][cols-1] == 'O':
                traverse(row, cols-1)
                
        for col in range(cols):
            if board[0][col] == 'O':
                traverse(0, col)
            if board[rows-1][col] == 'O':
                traverse(rows-1, col)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'