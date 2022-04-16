class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = {}
        n = len(ppid)
        
        for i in range(n):
            if ppid[i] not in tree: tree[ppid[i]] = [] #init parents
            tree[ppid[i]] += [pid[i]]
            
        res = [kill]
        
        def dfs(i):
            nonlocal res
            if i not in tree: return
            for child in tree[i]: 
                res += [child]
                dfs(child)
                
        dfs(kill)
        return res