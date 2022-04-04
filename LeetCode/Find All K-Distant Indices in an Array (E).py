class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        idxs = []
        for i in range(len(nums)):
            if nums[i] == key: idxs += [i]
                
        res = []
        for i in range(len(nums)):
            if not idxs: break
            if i > idxs[0]+k: idxs.pop(0)
                
            if idxs and (idxs[0]-k <= i <= idxs[0]+k):
                res += [i]
            
        return res