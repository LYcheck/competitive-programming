class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [ [0]*n for i in range(n) ]
        
        for _ in range(n):
            dp[_][_] = 1
        
        for sublen in range(2, n+1):
            for i in range(n-sublen+1):
                j = i + sublen - 1

                if(s[i] == s[j] and sublen == 2):
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                    
        return dp[0][n-1]