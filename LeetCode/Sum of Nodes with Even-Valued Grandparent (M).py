# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        leafsum = 0
        
        def add(left, right):
            nonlocal leafsum
            
            if left:
                if left.left:
                    leafsum += left.left.val
                if left.right:
                    leafsum += left.right.val
            if right:
                if right.left:
                    leafsum += right.left.val
                if right.right:
                    leafsum += right.right.val
                    
        
        def recurse(root):
            if not (root.val & 1):
                add(root.left, root.right)
                
            if root.left:
                recurse(root.left)
            if root.right:
                recurse(root.right)
            
            return
        
        recurse(root)
        
        return leafsum