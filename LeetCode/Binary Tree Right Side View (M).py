# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        curdepth = 0
        res = []
        
        def dfs(root, k):
            nonlocal curdepth
            
            if root:
                if k > curdepth:
                    res.append(root.val)
                    curdepth = k
                
                dfs(root.right, k+1)
                dfs(root.left, k+1)
            return
        
        dfs(root, 1)
        
        return res
            