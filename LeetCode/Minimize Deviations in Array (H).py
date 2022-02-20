from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] & 1: nums[i] *= 2
                
        slist = SortedList(nums)
        best = slist[-1]-slist[0]
        
        while not slist[-1] & 1:
            back = slist[-1]
            slist.pop(-1)
            slist.add(back//2)
            best = min(best, slist[-1]-slist[0])
        
        return best