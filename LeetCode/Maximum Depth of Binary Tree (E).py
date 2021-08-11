# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def traverse(root, ans1, ans2):
            if not root:
                return 0
            else:
                ans1 = traverse(root.left, ans1, ans2)
                ans2 = traverse(root.right, ans1, ans2)
                return max(ans1, ans2)+1
        
        ans1, ans2 = 0, 0
        
        return traverse(root, ans1, ans2)
