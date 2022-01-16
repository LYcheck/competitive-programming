# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t, h = head, head
        if not head or not t.next: return None
        
        t = t.next
        h = h.next.next
        while t != h:
            if not h or not h.next: return None
            t = t.next
            h = h.next.next
            
        h = head
        
        while t != h:
            t = t.next
            h = h.next
            
        return t