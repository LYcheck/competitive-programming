# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 1
        
        def recurse(node, val, temp):
            if node:
                if node.val == val+1:
                    temp += 1
                    nonlocal res
                    res = max(res, temp)
                else:
                    temp = 1
                    
                recurse(node.left, node.val, temp)
                recurse(node.right, node.val, temp)
        
        if not root: return 0
        recurse(root, -float('inf'), 1)
        return res