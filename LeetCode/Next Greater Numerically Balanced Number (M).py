class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        ptr = n+1
        
        while 1:
            num = str(ptr)
            ok = 1
            for i in num:
                ok &= (num.count(i) == int(i))
            
            if ok:
                break
                
            ptr += 1
        
        return ptr