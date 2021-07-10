class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = 0
        twice = 0
        
        for x in range(len(nums)):
            once = (nums[x] ^ once) & ~twice
            twice = (nums[x] ^ twice) & ~once
        return once
        
