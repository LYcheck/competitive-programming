# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxdif = 0
        
        def dfs(root, maxsofar, minsofar):
            nonlocal maxdif
            
            if not root: return
            
            maxdif = max(maxdif, abs(maxsofar-root.val), abs(minsofar-root.val))
            
            maxsofar, minsofar = max(maxsofar, root.val), min(minsofar, root.val)
            
            dfs(root.left, maxsofar, minsofar)
            dfs(root.right, maxsofar, minsofar)
                
            return
        
        dfs(root, root.val, root.val)
        return maxdif