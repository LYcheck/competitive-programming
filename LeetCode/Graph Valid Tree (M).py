class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(nodes, targ):
            if nodes[targ] == -1:
                return targ
            else:
                return find(nodes, nodes[targ])
        
        nodes = [-1]*n
        for i in range(len(edges)):
            x = find(nodes, edges[i][0])
            y = find(nodes, edges[i][1])
            
            if x == y: return False
            nodes[x] = y
            
        return len(edges) == n-1
            
            