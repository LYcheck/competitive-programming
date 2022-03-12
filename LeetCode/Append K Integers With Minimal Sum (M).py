class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        def sumuntil(s, f):
            more = (f*(f+1))//2
            less = (s*(s+1))//2
            return more-less-f
        
        nums.sort()
        ctr = 0
        res = 0
        start = 0
        
        for i in range(len(nums)):
            nx = nums[i]
            if start == nx: continue
            if nx-start-1 + ctr <= k:
                res += sumuntil(start, nx)
                ctr += nx-start-1
            else:
                res += sumuntil(start, start+(k-ctr+1))
                ctr = k
            
            start = nx
            if ctr == k: break 
            
        
        if ctr != k:
            res += sumuntil(start, start+(k-ctr+1))
            
        return res