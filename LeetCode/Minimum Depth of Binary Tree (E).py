# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int: 
        def dfs(root, k):
            if root:
                if not (root.left or root.right):
                    return k
                
                return min(dfs(root.left, k+1), dfs(root.right, k+1))
            
            else:
                return float('inf')
        
        return dfs(root, 1) if root else 0
            