class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = dict()
        
        for _ in nums:
            if _ in freq:
                freq[_] += 1
            else:
                freq[_] = 1
        
        nums = sorted(freq.keys())
        n = len(nums)
        
        onebefore = 0
        cur = nums[0]*freq[nums[0]]
        
        for i in range(1, n):
            val = nums[i]*freq[nums[i]]
            
            if nums[i]-nums[i-1] == 1:
                onebefore, cur = cur, max(onebefore+val, cur)
            else:
                onebefore, cur = cur, cur+val
                
        return cur