# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        heap = []
        ptrList = []
        
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        
        sentinel = ListNode(-1)
        curr = sentinel
        
        while heap:
            val, idx = heapq.heappop(heap)
            node = lists[idx]
            
            curr.next = node
            curr = curr.next
            lists[idx] = lists[idx].next
            
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            
        return sentinel.next
            