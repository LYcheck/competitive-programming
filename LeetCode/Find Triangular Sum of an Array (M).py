class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while 1:
            temp = []
            if len(nums) == 1: return nums[0]
            for i in range(1, len(nums)):
                temp += [(nums[i-1] + nums[i])%10]
            nums = temp
            
        