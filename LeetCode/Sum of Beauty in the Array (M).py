class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        minarr = [0 for x in range(n)]
        bigarr = [0 for x in range(n)]
        
        minarr[0] = nums[0]
        bigarr[n-1] = nums[n-1]
        
        for i in range(1,n):
            minarr[i] = max(nums[i], minarr[i-1])
            
        for i in range(n-2, -1, -1):
            bigarr[i] = min(nums[i], bigarr[i+1])
            
        res = 0
        print(minarr)
        print(bigarr)
        for i in range(1,n-1):
            if minarr[i-1] < nums[i] < bigarr[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            print(res, i)

            
                
        return res