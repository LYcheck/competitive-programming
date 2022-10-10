# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        q = [root]
        ctr = 1
        
        while q:
            temp = []
            for c in q:
                if c.left: temp += [c.left]
                if c.right: temp += [c.right]
                
            if ctr&1:
                l, r = 0, len(temp)-1
                while l < r:
                    temp[l].val, temp[r].val = temp[r].val, temp[l].val
                    l += 1
                    r -= 1
                
            q = temp
            ctr += 1
            
        return root
                    
                    