class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)     
        
        def populate(dir, ref):
            arr = [float('inf')]*n
            for i, v in enumerate(ref):
                if v == dir:
                    arr[i] = 0
                elif v == '.':
                    if i != 0: arr[i] = arr[i-1] + 1
                else: pass
            return arr
                    
        toright = populate('R', dominoes)
        toleft = populate('L', dominoes[::-1])[::-1]
        
        res = ''
        
        for i in range(n):
            res = res+'.' if toleft[i] == toright[i] else res+'R' if toright[i] < toleft[i] else res + 'L'
        return res