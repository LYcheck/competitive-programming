class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        chosen = [0]*length
        res = []
        temp = []
        
        def backtrack():
            if len(temp) == length:
                res.append(list(temp))
            else:
                for _ in range(length):
                    if chosen[_]:
                        continue
                    temp.append(nums[_])
                    chosen[_] = 1
                    backtrack()
                    temp.pop()
                    chosen[_] = 0
        
        backtrack()
        nres = []
        
        for ele in res:
            if ele not in nres:
                nres.append(ele)
                
        return nres