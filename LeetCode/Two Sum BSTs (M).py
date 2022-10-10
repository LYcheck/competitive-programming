# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        #this question sucks lol im not doing it the way they want me to
        
        have1 = {}
        have2 = {}
        
        def trav(node, mapp):
            if node:
                if node.val not in mapp:
                    mapp[node.val] = 1
                trav(node.left, mapp)
                trav(node.right, mapp)
                
        trav(root1, have1)
        trav(root2, have2)
        for _ in have1.keys():
            targ = target-_
            if targ in have2: return True
            
        return False