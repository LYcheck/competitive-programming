class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        
        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = dp[2] = 1
        
        for _ in range(3, n+1):
            dp[_] = dp[_-1] + dp[_-2] + dp[_-3]
        print(dp)
        return dp[n]