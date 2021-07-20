class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        temp = []
        
        def search(k):
            if k == n:
                res.append(list(temp))
            else:
                search(k+1)
                temp.append(nums[k])
                search(k+1)
                temp.pop()
                
        search(0)
        return res
