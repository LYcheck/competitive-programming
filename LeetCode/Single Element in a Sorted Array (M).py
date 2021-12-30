class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #1 1 3 3 5 7 7 9 9
        #0 1 2 3 4 5 6 7 8
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            m = (l+r)//2
            
            if (not m & 1 and nums[m+1] == nums[m]) or (m & 1 and nums[m-1] == nums[m]):
                l = m+1
            else:
                r = m
                
        return nums[l]
                
        
#          while l < r:
#             m = (l+r)//2
            
#             if not m & 1:
#                 if nums[m+1] == nums[m]:
#                     l = m+1
#                 else:
#                     r = m
#             else:
#                 if nums[m-1] == nums[m]:
#                     l = m+1
#                 else:
#                     r = m