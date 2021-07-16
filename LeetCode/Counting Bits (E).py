class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        
        for x in range(1, n+1):
            dp[x] = dp[x//2]
            
            if x & 1:
                dp[x] += 1
                
        return dp
        
