from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         left = 0
#         right = k
        
#         res = list()
        
#         while right < len(nums)+1:
#             res.append(max(nums[slice(left,right)]))
#             left += 1
#             right += 1
        
#         return res
        
        res = []
        deq = deque()
        left = right = 0
        
        while right < len(nums):
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            
            deq.append(right)
            
            if right+1 >= k:
                res.append(nums[deq[0]])
                left += 1
            right += 1
            
            if left > deq[0]:
                deq.popleft()
            
        return res
