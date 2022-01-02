# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        temp = ListNode()
        temp.next = head
        
        p = temp
        c = head
        while c and c.next:
            p.next = c.next
            p = p.next
            c.next = p.next
            p.next = c
            p = c
            c = c.next
            
        return temp.next
        
#         if not head:
#             return None
#         if not head.next:
#             return head
        
#         if not head.next.next:
#             temp = head.next
#             temp.next = head
#             head.next = None
#             return temp
        
#         def traverse(cur):
#             if cur.next and cur.next.next:
#                 temp1 = cur.next
#                 temp2 = cur.next.next
#                 temp3 = cur.next.next.next
#                 cur.next = temp2
#                 temp2.next = temp1
#                 temp1.next = temp3
        
#         temp = head.next
#         head.next = temp.next
#         temp.next = head
#         head = temp
            
#         f = head.next
#         ctr = 1
            
#         while f:
#             if ctr & 1:
#                 traverse(f)
                
#             ctr += 1
#             f = f.next
            
            
#         return head