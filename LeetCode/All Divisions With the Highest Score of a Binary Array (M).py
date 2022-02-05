class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = list(nums)
        
        for _ in range(n-2, -1, -1):
            r[_] += r[_+1]

        
        for _ in range(n):
            if nums[_]: nums[_] = 0
            else: nums[_] = 1
            
        l = list(nums)
        
        for _ in range(1, n):
            l[_] += l[_-1]
        
            
        scores = {}
        
        for i in range(n+1):
            left, right = -1, -1
            
            if i == 0:
                left = 0
                right = r[0]
            elif i == n:
                left = l[n-1]
                right = 0
            else:
                left = l[i-1]
                right = r[i]
                
            score = left+right
                
            if score in scores:
                scores[score] += [i]
            else:
                scores[score] = [i]
        
        keys = list(scores.keys())
        return scores[max(keys)]