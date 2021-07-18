class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arithSum = n*(n+1)//2
        
        return arithSum - sum(nums)

    def missingNumber(self, nums: List[int]) -> int:
        ans, _ = 0, 0
        
        for _ in range(len(nums)):
            ans ^= nums[_]
            ans ^= _
            
        return (ans ^ (_+1))
