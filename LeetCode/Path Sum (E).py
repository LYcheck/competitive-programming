# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(root, cur):
            if root:
                if not (root.left or root.right):
                    return cur + root.val == targetSum
                else:
                    return dfs(root.left, cur + root.val) or dfs(root.right, cur + root.val)
            return 
                
        return dfs(root, 0) if root else False