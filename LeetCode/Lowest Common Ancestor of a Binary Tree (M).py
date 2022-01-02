# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':   
        def find(root):
            if not root: return None
            if root.val == p.val or root.val == q.val: return root
            
            leftNode = find(root.left)
            rightNode = find(root.right)
            
            if leftNode and rightNode: return root
            else: return leftNode if leftNode else rightNode

        return find(root)