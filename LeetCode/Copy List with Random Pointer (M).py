"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#what a terrible solution. fix at some point

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        newNodes = {}
        nodeIdx = {}
        seen = {}
        
        ctr = 0
        temp = head
        while temp:
            seen[temp] = ctr
            temp = temp.next
            ctr += 1
        
        temp = head
        ctr = 0
        while temp:
            newNodes[ctr] = Node(x=temp.val)
            if temp.random: nodeIdx[temp.random] = seen[temp.random]
            ctr += 1
            temp = temp.next
        
        ctr = 0
        temp = head
        while temp:
            if ctr+1 in newNodes: newNodes[ctr].next = newNodes[ctr+1]
            if temp.random:
                newNodes[ctr].random = newNodes[nodeIdx[temp.random]]
            temp = temp.next
            ctr += 1
                
        return newNodes[0]