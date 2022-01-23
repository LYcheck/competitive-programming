class Solution:
    def countElements(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num in seen: seen[num] += 1
            else: seen[num] = 1
                
        keys = list(seen.keys())
        keys.sort()
        
        res = 0
        for i in range(len(keys)):
            if i != 0 and i < len(keys)-1:
                res += seen[keys[i]]
                
        return res