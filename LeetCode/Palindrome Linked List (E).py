# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def printl(node):
            while node:
                print(node.val, "", end="")
                node = node.next
                
        if not head.next: return True
        n = 0
        fast, slow = head, head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        s,c,f = None, slow, slow.next
        while c:
            c.next = s
            s = c
            c = f
            if f: f = f.next
        
        while head and s:
            if s.val != head.val: return False
            s, head = s.next, head.next
            
        return True
