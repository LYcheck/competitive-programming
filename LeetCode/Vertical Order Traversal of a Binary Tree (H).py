# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        havemap = {}
        #(node, xcoord, ycoord)
        q = [(root, 0, 0)]
        res = []
        
        while q:
            cur, curx, cury = q[0][0], q[0][1], q[0][2]
            q.pop(0)
            
            if curx in havemap: havemap[curx] += [(cury, cur.val)]
            else: havemap[curx] = [(cury, cur.val)]
                
            if cur.left: q += [(cur.left, curx-1, cury+1)]
            if cur.right: q += [(cur.right, curx+1, cury+1)]
                
        for k in sorted(havemap.keys()):
            res += [[x[1] for x in sorted(havemap[k])]]
            
        return res