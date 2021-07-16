class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in range(1, len(nums)):
            nums[n] ^= nums[n-1]
        
        return nums[-1]
