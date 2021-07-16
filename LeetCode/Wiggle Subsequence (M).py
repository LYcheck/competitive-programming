class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        ch1 = 1
        ch2 = 1
        
        for n in range(1, len(nums)):
            if nums[n] > nums[n-1]:
                ch1 = ch2 + 1
            elif nums[n] < nums[n-1]:
                ch2 = ch1 + 1
                
        if ch1 > ch2:
            return ch1
        else:
            return ch2
