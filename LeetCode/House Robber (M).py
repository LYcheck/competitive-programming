class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
       
        for _ in range(2,n):
            dp[_] = max(nums[_] + dp[_-2], dp[_-1])
                        
        return dp[n-1]
        
#         dp1, dp2 = 0, 0

#         for _ in nums:
#             temp = dp1
#             dp1 = dp2
#             dp2 = max(temp+_, dp2)

#         return dp2