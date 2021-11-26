class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = list(nums)
        
        minx = nums[0]
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]
            minx = min(minx, pref[i])
            
        if minx < 0:
            return abs(minx)+1
        
        else:
            return 1
        