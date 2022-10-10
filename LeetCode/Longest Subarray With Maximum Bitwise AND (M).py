class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxand = max(nums)
        res, ctr = 0, 0
        
        for i in range(n):
            if nums[i] == maxand:
                if ctr: ctr += 1
                else: ctr = 1
            else:
                ctr = 0
                
            res = max(ctr, res)
        return res