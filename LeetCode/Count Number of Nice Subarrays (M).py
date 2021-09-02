class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = []
        
        for i in range(len(nums)):
            if nums[i] & 1:
                odds.append(i)
        
        numsl = len(nums)
        oddsl = len(odds)
        
        if oddsl < k:
            return 0
        elif oddsl == k:
            return (odds[0]+1)*(numsl-odds[k-1])
        
        odds = [-1] + odds
        
        l, res = 1, 0
        
        odds.append(numsl)

        for r in range(k, oddsl+1):
            res += (odds[l]-odds[l-1])*(odds[r+1]-odds[r])
            l+=1 
        
        return res