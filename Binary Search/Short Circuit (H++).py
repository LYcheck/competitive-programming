class Solution:
    def solve(self, words):
        adj = [[] for i in range(26)]
        seen = [0]*26

        def dfs(s, visbruh):
            visbruh[s] = 1
            for node in adj[s]:
                if not visbruh[node]: dfs(node, visbruh)

        def isConnected(s):
            vis = [0]*26
            dfs(s, vis)

            for i in range(26):
                if not vis[i] and seen[i]: return False
            return True

        indeg, outdeg = [0]*26, [0]*26
        

        for w in words:
            w = w.lower()
            u, v = ord(w[0]) - ord('a'), ord(w[-1]) - ord('a')
            outdeg[u] += 1
            indeg[v] += 1
            adj[u] += [v]
            seen[u] = seen[v] = 1
        
        for i in range(26):
            if indeg[i] != outdeg[i]: return False
        
        return isConnected(ord(words[0][0].lower()) - ord('a'))

        