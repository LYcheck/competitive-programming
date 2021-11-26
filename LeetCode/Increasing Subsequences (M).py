class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(idx, temp):
            if idx > n-1:
                if len(temp) >= 2:
                    res.append(list(temp))
                return
                
            if not temp or nums[idx] >= temp[-1]:
                backtrack(idx+1, temp+[nums[idx]])
                
            if idx > 0 and len(temp) > 0 and nums[idx] == temp[-1]:
                return
            
            backtrack(idx+1, temp)
            
        backtrack(0, [])
        
        return res