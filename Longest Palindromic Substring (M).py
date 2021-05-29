class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def newString(s: str) -> str:
            sn = '#'
            for x in s:
                sn += x
                sn += '#'
            return sn
    
        sn = newString(s)
        leng = len(sn)
        
        p = [0] * leng
        c = 0
        cn = 0
        r = 0
        lmax = 0
        
        for i in range(leng):
            mir = 2*c - i
            
            if i < r:
                p[i] = min(r-i, p[mir])
            
            a = i + (1 + p[i])
            b = i - (1 + p[i])
            
            while(a < leng and b >= 0 and sn[a] == sn[b]):
                p[i] += 1
                a += 1
                b -= 1
                
            if (i + p[i]) > r:
                c = i
                r = i + p[i]
                
                if p[i] > lmax:
                    lmax = p[i]
                    cn = i
                    
        return s[cn//2-lmax//2:cn//2+ceil(lmax/2)]
