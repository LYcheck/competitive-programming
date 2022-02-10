class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        best = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2+dp[i-2] if i >= 2 else 2
                else:
                    if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                        dp[i] = dp[i-1] + dp[i-2-dp[i-1]] + 2
                        
                    
            best = max(best, dp[i])
        
        print(dp)
        return best