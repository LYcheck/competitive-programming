class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if int(s[0]) != 0:
            dp[1] = 1
        
        for _ in range(2, len(s)+1):
            if s[_-1] != '0':
                dp[_] += dp[_-1]
            if s[_-2:_] > '09' and s[_-2:_] < '27':
                dp[_] += dp[_-2]

                       
        return dp[-1]
