class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = list(nums), list(nums)
        if len(nums) == 1: return 0
        
        for i in range(1, len(nums)):
            l[i] += l[i-1]
            r[~i] += r[~i+1]

        if r[1] == 0: return 0
        for i in range(1, len(nums)-1):
            print(i, l[i], r[i])
            if l[i-1] == r[i+1]: return i
            
        if l[-2] == 0: return len(nums)-1
        
        return -1