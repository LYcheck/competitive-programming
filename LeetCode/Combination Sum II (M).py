class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(temp, idx, targ):
            if targ < 0:
                return
            
            elif targ == 0:
                res.append(temp)
                return
            
            for i in range(idx, len(candidates)):
                if idx < i and candidates[i] == candidates[i-1]:
                    continue
                    
                dfs(temp+[candidates[i]], i+1, targ-candidates[i])
        
        candidates.sort(reverse=True)
        res = []
        dfs([], 0, target)

        return res
