class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        resmax = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                temp = nums[j] - nums[i]
                
                if temp > resmax:
                    resmax = temp
                    
        return resmax