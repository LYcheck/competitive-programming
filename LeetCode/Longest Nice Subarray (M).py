class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # pigeonhole principle explanation for ridiculous runtime: each window size
        # can be at most 32, since each subset must contain at most 1 set bit per 
        # bit position, restricting the runtime to a coefficient of linear
        l = 0
        def check(left, right):
            for i in range(left, right+1):
                for j in range(i+1, right+1):
                    if nums[i] & nums[j] != 0: return False
            return True
        
        res = 1
        for i in range(1, len(nums)):
            while not check(l, i): 
                l += 1
            res = max(res, i-l+1)
            
        return res