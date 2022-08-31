class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suf = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] = nums[i]*nums[i-1] if nums[i-1] != 0 else nums[i]
            suf[i] = suf[i]*suf[i-1] if suf[i-1] != 0 else suf[i]
                
        return max(nums+suf)