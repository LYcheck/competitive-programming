# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head
        
        slow = head
        evenStart = head.next
        fast = head.next
        
        while fast and fast.next:
            temp = fast.next
            fast.next = fast.next.next
            temp.next = evenStart
            slow.next = temp
            if fast: fast = fast.next
            slow = temp
            
        return head