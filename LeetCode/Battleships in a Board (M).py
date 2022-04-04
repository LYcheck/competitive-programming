class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        cnt = 0
        
        for row in range(rows):
            for col in range(cols):
                flagx = col == 0 or board[row][col-1] == '.'
                flagy = row == 0 or board[row-1][col] == '.'
                #corner
                if board[row][col] == 'X' and flagx and flagy: cnt += 1
                    
        return cnt