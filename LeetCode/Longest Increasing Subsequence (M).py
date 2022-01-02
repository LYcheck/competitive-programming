class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles = []
        
        for num in nums:
            if not piles:
                piles.append([num])
                continue
            
            l, r = 0, len(piles)-1
            
            while l < r:
                m = (l+r)//2
                if num > piles[m][-1]:
                    l = m+1
                else:
                    r = m
            
            if piles[l][-1] < num:
                piles.append([num])
            else:
                piles[l].append(num)
        
        print(piles)
        return len(piles)
        
#         O(N)
#         dp = [1]*len(nums)
#         maxsofar = 1
        
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j]+1)
#                     maxsofar = max(maxsofar, dp[i])
                    
#         return maxsofar