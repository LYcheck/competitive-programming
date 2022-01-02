class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        nums = nums
        ans = [None]*n
        
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        for i in range(n):
            if i < k or i > n-1-k:
                ans[i] = -1
            else:
                num1 = nums[i+k]
                num2 = nums[i-k-1]
                if i-k-1 == -1:
                    num2 = 0

                ans[i] = (num1-num2)//(2*k+1)

        return ans