# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        cursum = 0
        def dfs(root, temp):
            nonlocal cursum
            
            if root:
                temp *= 10
                temp += root.val
                if not (root.left or root.right):
                    cursum += temp
                    return
                else:
                    dfs(root.left, temp)
                    dfs(root.right, temp)
                    return
            return
        
        dfs(root, 0)
        return cursum