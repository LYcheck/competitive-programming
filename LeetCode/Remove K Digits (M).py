class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        
        for i in num:
            curr = int(i)
            while k > 0 and stk and int(stk[-1]) > curr:
                k -= 1
                stk.pop(-1)
                
            stk += [i]
        
        if k: stk = stk[:-k]
        return ''.join(stk).lstrip('0') or '0'
