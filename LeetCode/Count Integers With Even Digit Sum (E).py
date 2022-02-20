class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1,num+1):
            val = 0
            for j in str(i):
                val += int(j)
                
            if not val & 1:
                res += 1
                
        return res