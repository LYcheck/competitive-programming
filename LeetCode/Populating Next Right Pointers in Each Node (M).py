"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nextNode = root
        
        while nextNode:
            node = nextNode
            
            while node:
                if node.left:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
                node = node.next
            
            nextNode = nextNode.left
        
        return root