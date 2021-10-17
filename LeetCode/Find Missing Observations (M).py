class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        
        num = mean*(m+n)
        for _ in rolls:
            num -= _
        
        res = []
        
        if num / n > 6 or num / n < 1:
            return res
        
        temp = num // n
        while len(res) != n:   
            res.append(temp)
            num -= temp
                    
        idx = 0
        while num != 0:
            if res[idx] == 6:
                idx += 1
            else:
                res[idx] += 1
                num -= 1
        
        return res if len(res) == n else []