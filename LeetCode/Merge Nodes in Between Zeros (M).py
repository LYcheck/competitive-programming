# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursum = 0
        temp = ListNode()
        dummy = temp
        head = head.next
        setFlag = 0
        
        while head:
            if head.val == 0: setFlag = 1
            
            cursum += head.val
            
            if setFlag:
                temp.next = ListNode(val=cursum)
                temp = temp.next
                cursum = 0
                setFlag = 0
                
            head = head.next
                
        return dummy.next