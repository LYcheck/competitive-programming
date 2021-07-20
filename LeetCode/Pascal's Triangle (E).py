Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for _ in range(numRows):
            temp = []
            for i in range(_+1):
                temp.append(comb(_, i))
            res.append(temp)
            
        return res
