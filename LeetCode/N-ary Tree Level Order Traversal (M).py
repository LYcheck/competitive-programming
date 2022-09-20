"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        q = [(root, 0)]
        res = [[]]
        proc = 0
        
        while q:
            cur = q[0][0]
            dep = q[0][1]
            q.pop(0)
            for _ in cur.children:
                q += [(_, dep+1)]
            if proc >= dep:
                res[dep] += [cur.val]
            else:
                res += [[cur.val]]
                proc += 1

        return res