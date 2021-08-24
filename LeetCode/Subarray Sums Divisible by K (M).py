class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0]*n
        pref[0] = nums[0]
        
        for _ in range(1, n):
            pref[_] = pref[_-1] + nums[_]
            
        
        