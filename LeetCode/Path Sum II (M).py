# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, temp, sumTo):
            nonlocal res
            if root:
                if not (root.left or root.right) and sumTo + root.val == targetSum:
                    temp.append(root.val)
                    res.append(list(temp))
                    return
                else:
                    dfs(root.left, temp + [root.val], sumTo + root.val)
                    dfs(root.right, temp + [root.val], sumTo + root.val)
                    return
            return
        
        if root:
            dfs(root, [], 0)
        return res