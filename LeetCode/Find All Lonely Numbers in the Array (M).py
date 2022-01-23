class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = {}
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        
        res = []
        for num in nums:
            if (num+1) not in seen and (num-1) not in seen and seen[num] == 1:
                res.append(num)
        
        return res