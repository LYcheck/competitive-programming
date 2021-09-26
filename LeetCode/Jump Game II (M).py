#DP method
class Solution:
    def jump(self, nums: List[int]) -> int:
        s = len(nums)
        
        dp = [float('inf')]*(s+1)
        dp[0] = 0
        
        for i in range(s):
            for j in range(1,nums[i]+1):
                if i + j <= s:
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        
        return dp[s-1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        level, curEnd, nextEnd = 0, 0, 0
        
        for i in range(n):
            if i > curEnd:
                curEnd = nextEnd
                level += 1
            nextEnd = max(nextEnd, i + nums[i])
        
        return level