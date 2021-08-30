# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        leafsum = 0
        temp = 0
        
        def recurse(root, cnt):
            nonlocal leafsum
            nonlocal temp
            
            if not (root.left or root.right):
                if cnt > temp:
                    leafsum = root.val
                    temp = cnt
                elif cnt == temp:
                    leafsum += root.val
                    
            if root.left:
                recurse(root.left, cnt+1)
            if root.right:
                recurse(root.right, cnt+1)
            
            return
        
        recurse(root, 0)
        
        return leafsum