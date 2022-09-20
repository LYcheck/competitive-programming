class Solution:
    def solve(self, nums):
        if not nums: return 0
        flag1, flag2 = 1, 0
        c1, c2 = 1, 1

        for i in range(1, len(nums)):
            dif = (nums[i] - nums[i-1]) > 0
            if nums[i] == nums[i-1]: continue

            if flag1^dif:
                c1 += 1
                flag1 = not flag1
            if flag2^dif:
                c2 += 1
                flag2 = not flag2

        return max(c1,c2)