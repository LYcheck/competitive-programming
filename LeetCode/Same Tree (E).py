# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSame(p, q):
            if p and q:
                ans = (p.val == q.val) and isSame(p.left, q.left) and isSame(p.right, q.right)
                return ans
            return p == q

        return isSame(p, q)
