# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stk = []
        
        def dfs(root):
            if not root: return None
            
            nonlocal stk
            temp = dfs(root.left)
            if temp: stk += [temp]
            stk += [root]
            temp = dfs(root.right)
            if temp: stk += [temp]
                
        dfs(root)
        
        if stk: root = stk[0]
            
        for i in range(len(stk)-1):
            stk[i].right = stk[i+1]
            stk[i].left = None
            
            stk[i+1].right = None
            stk[i+1].left = None
            
        return root
            