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

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        o1, o2 = 1, 0
        o1c, o2c = 1, 1
        
        for i in range(1, len(nums)):
            diff = nums[i]-nums[i-1] > 0
            if nums[i]-nums[i-1] == 0:
                continue
            
            if diff ^ o1:
                o1 = not o1
                o1c += 1
            if diff ^ o2:
                o2 = not o2
                o2c += 1
                
        return max(o1c, o2c)