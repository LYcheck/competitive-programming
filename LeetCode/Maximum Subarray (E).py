class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
#         best, cur = float('-inf'), float('-inf')
        
#         for dig in nums:
#             cur = max(dig, cur + dig)
#             best = max(cur, best)
            
#         return best

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        res = -float('inf')
        minprefix = nums[0]

        for j in range(len(nums)):
            res = max(res, nums[j]-minprefix)
            minprefix = min(nums[j], minprefix)
        
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        best = dp[0]
        
        for i in range(1, n):
            dp[i] = nums[i] + dp[i-1] if dp[i-1] > 0 else nums[i]
            best = max(best, dp[i])
            
        return best