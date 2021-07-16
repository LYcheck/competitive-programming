class Solution {
public:
    int climbStairs(int n) {
        if(n == 1) return 1;

        int dp[n];
        dp[0] = 1;
        dp[1] = 2;

        for(int i = 2; i < n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n-1];
    }

// #         def rec(n):
// #             if n == 1 or n == 0:
// #                 return 1
// #             elif n in dp:
// #                 return dp[n]
// #             else:
// #                 dp[n] = rec(n-1) + rec(n-2)
// #                 return dp[n]

// #         return rec(n)

};