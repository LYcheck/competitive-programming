class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]
        for i in range(1, len(nums)):
            res = gcd(res, nums[i])
            if nums[i] == 1 or res == 1: return 1
        return 0 if res != 1 else 1