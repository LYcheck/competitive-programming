# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(cur, parent, grandparent):
            if not cur: return
            
            if grandparent and not grandparent.val & 1:
                nonlocal res
                res += cur.val
                
            dfs(cur.left, cur, parent)
            dfs(cur.right, cur, parent)
            
        dfs(root, None, None)
        return res