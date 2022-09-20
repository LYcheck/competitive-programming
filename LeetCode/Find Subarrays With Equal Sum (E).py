class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        have = {}
        for i in range(1, len(nums)):
            cur = nums[i-1] + nums[i]
            if cur in have: return True
            have[cur] = 1
            
        return False