# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def travel(node, maxso):
            if node:
                if node.val >= maxso:
                    nonlocal res
                    res += 1
                    
                travel(node.left, max(node.val, maxso))
                travel(node.right, max(node.val, maxso))
                
        if not root: return 0
        travel(root, -float('inf'))
        return res