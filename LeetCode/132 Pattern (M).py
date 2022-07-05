class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        curm = -float('inf')
        
        for i in range(len(nums)-1, -1, -1):
            while(stk and nums[i] > stk[-1]): 
                curm = stk[-1]
                stk.pop(-1)
            
            if curm > nums[i]: return True
            elif curm < nums[i]: stk += [nums[i]]
            else: continue
            
        return False