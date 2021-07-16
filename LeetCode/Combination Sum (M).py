class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(res, temp, nums, targ):
            if targ < 0:
                return
            
            elif targ == 0:
                res.append(temp)
                return
            
            for i in range(len(nums)):
                dfs(res, temp+[nums[i]], nums[i:], targ-nums[i])
                    
        res = []
        dfs(res, [], candidates, target)
        return res
