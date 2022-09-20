class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax, maxsum, curmin, minsum = 0, nums[0], 0, nums[0]
        cs = 0
        
        for _ in nums:
            curmax = max(curmax + _, _)
            maxsum = max(curmax, maxsum)
            curmin = min(curmin + _, _)
            minsum = min(curmin, minsum)
            
            cs += _
            
        return max(maxsum, cs-minsum) if maxsum > 0 else maxsum