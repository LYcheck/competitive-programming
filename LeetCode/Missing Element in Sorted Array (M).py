class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i-1]
            
            if cur-prev <= 1: continue
            elif (cur-prev-1) >= k:
                return prev+k
            else:
                k -= (cur-prev-1)
                
                
        return nums[-1]+k