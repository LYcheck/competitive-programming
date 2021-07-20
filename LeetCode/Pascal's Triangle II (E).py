class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        
        for _ in range(rowIndex+1):
            res.append(comb(rowIndex, _))
            
        return res
