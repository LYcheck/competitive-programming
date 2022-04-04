class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen: seen[num] += 1
            else: seen[num] = 1
                
                
        for key in seen.keys():
            if seen[key] & 1: return False
            
        return True