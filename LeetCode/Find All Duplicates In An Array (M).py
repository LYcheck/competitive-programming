class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for _ in nums:
            idx = abs(_)-1
            if nums[idx] < 0:
                res.append(abs(_))
            
            nums[idx] = -nums[idx]
        
        return res
            
            