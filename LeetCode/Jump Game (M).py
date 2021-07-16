class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        
        for i in range(len(nums)-2, 0, -1):
            if nums[i] == 0:
                continue
            elif i + nums[i] >= target:
                target = i
            else:
                continue
        
        if target <= nums[0]:
            return True
        else:
            return False
