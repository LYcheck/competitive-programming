# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = []
        prev = None
        
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
                
            root = stk.pop()
            if prev and prev.val >= root.val: return False # checks uniquity aswell
            prev = root
            root = root.right
        
        return True