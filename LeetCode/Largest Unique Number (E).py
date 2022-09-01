class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        seen = {}
        cand = -1
        
        for _ in nums:
            if _ in seen: seen[_] += 1
            else: seen[_] = 1
                
                
        for k in seen.keys():
            if seen[k] == 1: cand = max(cand, k)
                
        return cand