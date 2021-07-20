class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(a):
            if len(temp) == k:
                res.append(list(temp))
            else:
                for _ in range(a, n+1):
                    temp.append(_)
                    backtrack(_+1)
                    temp.pop()
                    
        res = []
        temp = []
        backtrack(1)
        
        return res
