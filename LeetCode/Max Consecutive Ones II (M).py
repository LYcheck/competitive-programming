class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        l = -1
        zero = 0
        best = 0
        
        for r in range(n):
            if not nums[r]:
                if not zero:
                    zero = 1
                else:
                    l+=1
                    while nums[l]: l += 1
            best = max(best, r-l)
                    
        return best
                    