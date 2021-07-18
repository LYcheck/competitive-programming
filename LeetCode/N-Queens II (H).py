class Solution:
    def totalNQueens(self, n: int) -> int:

        def backtrack(y):
            if y == n:
                return 1
            cnt = 0
            
            for _ in range(n):
                if _ in cols or y-_ in diag1 or y+_ in diag2:
                    continue
                
                cols.add(_)
                diag1.add(y-_)
                diag2.add(y+_)

                cnt += backtrack(y+1)

                cols.remove(_)
                diag1.remove(y-_)
                diag2.remove(y+_)

            return cnt
        
        cols = set()
        diag1 = set()
        diag2 = set()
        return backtrack(0)
