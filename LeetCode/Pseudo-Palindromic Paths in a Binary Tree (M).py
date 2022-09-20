# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def validate(b):
            if not b or (b&(b-1) == 0): return 1
            return 0
        
        def dfs(node, bitset):
            if node:
                bitset ^= (1 << node.val)
                
                if not (node.left or node.right): return validate(bitset)
                return dfs(node.left, bitset) + dfs(node.right, bitset)
                
            return 0
        
        return dfs(root, 0)