# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        temp = head
        cnt = 1
        while temp.next:
            cnt += 1
            temp = temp.next
        
        k%=cnt
        
        slow, fast = head, head
        
        for i in range(k): fast = fast.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        fast.next = head
        toRet = slow.next
        slow.next = None
        
        return toRet