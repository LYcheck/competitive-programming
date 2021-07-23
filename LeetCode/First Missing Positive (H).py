class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        n = len(nums)
        
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        
        for j in range(len(nums)):
            nums[nums[j]%n] += n
        
        for k in range(1, len(nums)):
            if nums[k]//n == 0:
                return k
        return n
