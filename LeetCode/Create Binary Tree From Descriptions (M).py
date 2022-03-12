# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = {}
        children = {}
        for desc in descriptions:
            if desc[0] not in nodes:
                nodes[desc[0]] = TreeNode(val=desc[0])
            parents[desc[0]] = 1
            if desc[1] not in nodes:
                nodes[desc[1]] = TreeNode(val=desc[1])
            children[desc[1]] = 1
            
        for desc in descriptions:
            if desc[2]: nodes[desc[0]].left = nodes[desc[1]]
            else: nodes[desc[0]].right = nodes[desc[1]]
        
        for i in parents.keys():
            if i not in children: return nodes[i]