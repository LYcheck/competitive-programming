class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [0]*9
        rows = [0]*9
        squares = [0]*9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    k = board[i][j]
                    bit = 1 << int(k)
                    
                    if bit & rows[i] == bit:
                        return False
                    elif bit & cols[j] == bit:
                        return False
                    elif bit & squares[i//3*3+j//3] == bit:
                        return False
                    
                    rows[i] |= bit
                    cols[j] |= bit
                    squares[i//3*3+j//3] |= bit
                    
        return True