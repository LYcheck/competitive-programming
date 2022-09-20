class Solution:
    def solve(self, s):
        a, b = s, s[::-1]
        dp = [[-1 for i in range(len(b)+1)] \
        for j in range(len(a)+1)]

        res = 0
        for i in range(len(a)+1):
            for j in range(len(b)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] =   max(dp[i-1][j], \
                                        dp[i][j-1])
                res = max(res, dp[i][j])
   
        return res