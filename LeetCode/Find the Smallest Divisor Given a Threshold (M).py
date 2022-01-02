class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, 10000000
        
        while l < r:
            m = (l+r)//2
            
            runsum = 0
            for num in nums:
                runsum += ceil(num/m)
                
            if runsum > threshold:
                l = m+1
            else:
                r= m
                
        return l