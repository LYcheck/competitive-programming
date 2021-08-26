class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board[0])
        n = len(board)
        
        def dfs(word, board, i, j):
            if word == "":
                return True
            elif i < 0 or j < 0 or i >= n or j >= m:
                return False
            elif board[i][j] != word[0]:
                return False
            
            temp = board[i][j]
            board[i][j] = '.'
            
            restemp = dfs(word[1:], board, i+1, j) or dfs(word[1:], board, i, j+1) or dfs(word[1:], board, i-1, j) or dfs(word[1:], board, i, j-1)
            
            board[i][j] = temp
            return restemp
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(word, board, i, j):
                        return True
        return False