class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        have = {0:-1}
        runsum = 0
        for i, num in enumerate(nums):
            runsum+=num
            runsum%=k
            
            if runsum in have:
                if i-have[runsum]>1: return True
            else:
                have[runsum] = i
                
        return False