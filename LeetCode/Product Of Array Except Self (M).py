class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         arrayProd = 1
#         zeroCount = 0
#         # ans = [int]*len(nums)
        
#         for x in nums:
#             if x == 0:
#                 zeroCount += 1
#             else:
#                 arrayProd = arrayProd*x
        
#         for x in range(len(nums)):
#             if zeroCount > 1:
#                 nums[x] = 0
                
#             elif nums[x] == 0:
#                 nums[x] = arrayProd
                
#             elif zeroCount == 1:
#                 nums[x] = 0
                
#             else:
#                 nums[x] = arrayProd//nums[x]
                
#         return nums

        forw = list(nums)
        back = list(nums)
        n = len(nums)
        
        for _ in range(1, n):
            forw[_] *= forw[_-1]
            back[-_-1] *= back[-_]
            
        nums[0] = back[1]
        nums[n-1] = forw[n-2]
        
        for _ in range(1, n-1):
            nums[_] = forw[_-1] * back[_+1]
            
        return nums