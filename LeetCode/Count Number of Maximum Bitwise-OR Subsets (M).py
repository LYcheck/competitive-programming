class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = dict()
        n = len(nums)
        
        def backtrack(k, cor):
            if k == n:   
                if cor in subsets:
                    subsets[cor] += 1
                else:
                    subsets[cor] = 1
                    
            else:
                backtrack(k+1, cor)
                backtrack(k+1, cor | nums[k])

        backtrack(0, 0)
        curmax = -1
        for key in subsets:
            curmax = max(curmax, key)

        return subsets[curmax]