class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        for i in range(1,n): nums[i] += nums[i-1]
        
        def bs(idx, leftflag):
            root = nums[idx-1]
            l, r, res = idx, n-2, -1
            
            while l <= r:
                m = l+(r-l)//2
                left = nums[m]-nums[idx-1]
                right = nums[-1]-nums[m]
                
                if root <= left <= right:
                    res = m
                    if leftflag: r = m-1
                    else: l = m+1
                elif root > left:
                    l = m+1
                else:
                    r = m-1
            return res
                
        res = 0
        print(nums) 
        for i in range(1,n-1):
            if (nums[n-1]-nums[i-1]) / 2 < nums[i-1]: break
            
            leftidx = bs(i, True)
            rightidx = bs(i, False)
            if leftidx == -1 or rightidx == -1: continue
            res = (res + (rightidx-leftidx+1)%mod)%mod
        return res