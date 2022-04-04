class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [ 'a' for i in range(n) ]
        
        k -= n
        
        for i in range(n-1, -1, -1):
            if not k: break
                
            if k >= 25:
                res[i] = 'z'
                k -= 25
            else:
                res[i] = chr(ord('a')+k)
                break
                
        return ''.join(res)