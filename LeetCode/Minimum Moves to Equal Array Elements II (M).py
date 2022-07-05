class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        a = -1
        res = 0
        nums.sort()
        if len(nums) & 1:
            a = nums[len(nums)//2]
        else:
            a = round((nums[len(nums)//2-1]+nums[len(nums)//2])/2)
                           
        for num in nums:
            res += abs(a-num)
            
        return res
                           