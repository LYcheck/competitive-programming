class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arithSum = n*(n+1)//2
        
        return arithSum - sum(nums)
