class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for num in nums:
            tst = abs(num)
            if nums[tst-1] > 0:
                nums[tst-1] *= -1
                
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
                
        return res