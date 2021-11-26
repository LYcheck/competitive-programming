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