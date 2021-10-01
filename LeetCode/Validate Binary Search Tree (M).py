# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = None

        def traverse(root):
            if root:
                valid = traverse(root.left)

                if(not valid or prev != None and root and prev.val > root.val):
                    return False
                
                prev = root
                valid = traverse(root.right)

                return valid
            return True