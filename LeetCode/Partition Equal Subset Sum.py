class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        
        s //= 2
        
        dp = [0]*(s+1)
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(s, 0, -1):
                if j-nums[i] >= 0:
                    if dp[j-nums[i]] or dp[j]:
                        dp[j] = 1
        
        return dp[s]