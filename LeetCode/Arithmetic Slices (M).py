class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        sofar = 0
        ctr, flag = 0, 0
        prev2, prev1 = nums[0], nums[1]
        
        for i in range(2, n):
            curr = nums[i]
            diff = prev1-prev2
            
            if curr-prev1 == diff:
                if not ctr: ctr = 3
                else: ctr += 1
            else:
                flag = 1
            
            flag |= i == n-1
            
            if flag:
                for k in range(3, ctr+1):
                    sofar += ctr-k+1
                ctr = 0
                flag = 0
            
            prev2, prev1 = prev1, curr
    
        return sofar