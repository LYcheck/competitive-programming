class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt, i = 0, 0
        n = len(s)
        while i < n:
            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i+=1 
        return cnt