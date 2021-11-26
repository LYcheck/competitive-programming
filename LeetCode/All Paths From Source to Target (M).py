class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph)-1
        
        def backtrack(node, temp):
            if node == end:
                res.append(list(temp))
                return
            
            else:
                for i in graph[node]:
                    backtrack(i, temp+[i])
        
        backtrack(0, [0])
        
        return res