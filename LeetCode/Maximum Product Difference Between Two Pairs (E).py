class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        fmax = float('-inf')
        smax = float('-inf')
        fmin = float('inf')
        smin = float('inf')
        
        for _ in nums:
            if _ > fmax:
                smax = fmax
                fmax = _
            elif _ > smax:
                smax = _
            
            if _ < fmin:
                smin = fmin
                fmin = _
            elif _ < smin:
                smin = _
        
        return (fmax * smax) - (fmin * smin)
