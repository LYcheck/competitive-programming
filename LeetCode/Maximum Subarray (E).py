class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best, cur = float('-inf'), float('-inf')
        
        for dig in nums:
            cur = max(dig, cur + dig)
            best = max(cur, best)
            
        return best
