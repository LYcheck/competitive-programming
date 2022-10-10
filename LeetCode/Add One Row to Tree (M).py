# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val,left=root)
        q = [root]
        dep = 1
        
        
        while q:
            temp = []
            dep += 1
            for node in q:
                if node.left: temp += [node.left]
                if node.right: temp += [node.right]
            if dep == depth:
                ptr = 0
                for node in q:
                    if node.left:
                        node.left = TreeNode(val=val,left=temp[0])
                        temp.pop(0)
                    else: node.left = TreeNode(val=val)
                    if node.right:
                        node.right = TreeNode(val=val,right=temp[0])
                        temp.pop(0)
                    else: node.right = TreeNode(val=val)
                return root
            q = temp
            
        print(temp)