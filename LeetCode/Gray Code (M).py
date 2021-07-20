class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]
        
        for i in range(1, n):
            for _ in reversed(res):
                res.append(_+(2**(i)))
            
        return res
