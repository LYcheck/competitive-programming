class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if not nums[0]:
            return 0
        
#         res = nums[0] > 0
        
#         for i in range(1, len(nums)):
#             if nums[i] == 0:
#                 return 0
            
#             res = not (res ^ (nums[i]>0))
        
#         if not res:
#             return -1
#         else:
#             return 1

        count = 0
        for x in nums:
            if not x:
                return 0
            elif x < 0:
                count += 1
                
        if count & 1:
            return -1
        else:
            return 1
