class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        
        for i in range(len(nums)):
            if not stk or nums[i] < nums[stk[-1]]:
                stk.append(i)
        
        best = -float('inf')
        for i in range(len(nums)-1, -1 ,-1):
            while stk and nums[i] >= nums[stk[-1]]:
                best = max(best, i-stk.pop())
                
        return best