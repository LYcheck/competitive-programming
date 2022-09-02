# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        
        q = [root]
        res = []
        
        while q:
            csum, n = 0, len(q)
            for i in range(len(q)):
                cur = q[0]
                q.pop(0)
                csum += cur.val
                if cur.left: q += [cur.left]
                if cur.right: q += [cur.right]
                
            res += [csum/n]
        
        return res