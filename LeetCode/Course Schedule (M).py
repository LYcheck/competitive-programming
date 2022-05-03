class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { i:[] for i in range(numCourses) }
        visited = [0]*numCourses
        for cur, pre in prerequisites:
            graph[pre] += [cur]
            
        def dfs(cur):
            if visited[cur] == -1: return False # being visited, cycle
            if visited[cur] == 1: return True # visited, get out
            visited[cur] = -1 # mark visit
            
            for i in graph[cur]:
                if not dfs(i): return False # watch for cycle
            
            visited[cur] = 1
            return True
            
        for i in range(numCourses):
            if not dfs(i): return False
            
        return True