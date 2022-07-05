class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(idx, temp, cur):
            if len(temp) == k:
                if cur == n: 
                    nonlocal res
                    res += [list(temp)]
                return
            
            for i in range(idx, 10):
                if i + cur > n: return
                else: dfs(i+1, temp + [i], cur + i)
            
                
        dfs(1, [], 0)
        return res