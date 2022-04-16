class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        flag = 0
        n = len(nums)
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False
        
        
#         n = len(nums)
#         smallFromLeft = [float('inf')]*n
#         largeFromRight = [-float('inf')]*n
        
#         smallFromLeft[0] = nums[0]
#         largeFromRight[n-1] = nums[n-1]
        
#         for i in range(1,n):
#             smallFromLeft[i] = min(smallFromLeft[i-1], nums[i])
#             largeFromRight[~i] = max(largeFromRight[~i+1], nums[~i])
            
#         for i in range(1, n-1):
#             val = nums[i]
            
#             if smallFromLeft[i-1] < val < largeFromRight[i+1]: return True
            
#         return False