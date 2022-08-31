class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [1]*n
        
        def dfs(i):
            for j in range(n):
                if vis[j] and isConnected[i][j]:
                    vis[j] = 0
                    dfs(j)
                    
        
        cnt = 0
        for k in range(n):
            if vis[k]: 
                dfs(k)
                cnt += 1
            
        return cnt