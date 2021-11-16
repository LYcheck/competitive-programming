class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = []
        
        dp = [1]*n
        parents = [-1]*n
        best = -1
        ptr = 0
        
        for i in range(n):
            n1 = nums[i]
            for j in range(i):
                n2 = nums[j]
                
                if n1 % n2 == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j]+1
                        parents[i] = j

        for _ in range(1, n):
            if dp[_] > dp[ptr]:
                ptr = _
        
        while parents[ptr] != -1:
            res.append(nums[ptr])
            ptr = parents[ptr]
        res.append(nums[ptr])
        
        return res
