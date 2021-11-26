# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        
        if not cur:
            return head
    
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                
            else:
                cur = cur.next
                
        return head.next if head.val == val else head