class Solution:
    def solve(self, a, b, c):
        dp = [[[-1 for i in range(len(c)+1)] \
        for j in range(len(b)+1)] \
        for k in range(len(a)+1)]

        res = 0
        for i in range(len(a)+1):
            for j in range(len(b)+1):
                for k in range(len(c)+1):
                    if i == 0 or j == 0 or k == 0:
                        dp[i][j][k] = 0
                    elif a[i-1] == b[j-1] == c[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] =   max(dp[i-1][j][k], \
                                            dp[i][j-1][k], \
                                            dp[i][j][k-1])
                    res = max(res, dp[i][j][k])
   
        return res