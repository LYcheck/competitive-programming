class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        ddx, ddy = None, None
        res = 0
        stockPrices.sort(key=lambda x: x[0])
        
        for i in range(1, len(stockPrices)):
            px, py = stockPrices[i-1][0], stockPrices[i-1][1]
            x, y = stockPrices[i][0], stockPrices[i][1]
            
            if ddx == None:
                res = 1
                ddx, ddy = x-px, y-py
                d = gcd(ddx, ddy)
                ddx, ddy = ddx // d, ddy // d
                continue
            
            cdx = x-px
            cdy = y-py
            cdx, cdy = cdx // gcd(cdx, cdy), cdy // gcd(cdx, cdy)
            
            if ddx != cdx or ddy != cdy: res += 1
            
            ddx = cdx
            ddy = cdy
            
        return res