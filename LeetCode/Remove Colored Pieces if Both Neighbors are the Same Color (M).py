class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        mapa = dict()
        mapb = dict()
        
        curr = colors[0]
        cnt = 0
        
        for _ in colors:
            if _ == 'A' == curr:
                cnt += 1
            elif _ == 'B' == curr:
                cnt += 1
                
            elif curr == 'A':
                if cnt in mapa:
                    mapa[cnt] += 1
                else:
                    mapa[cnt] = 1
                curr = 'B'
                cnt = 1
            else:
                if cnt in mapb:
                    mapb[cnt] += 1
                else:
                    mapb[cnt] = 1
                curr = 'A'
                cnt = 1
        
        if curr == 'A':
            if cnt in mapa:
                mapa[cnt] += 1
            else:
                mapa[cnt] = 1
        
        elif curr == 'B':
            if cnt in mapb:
                mapb[cnt] += 1
            else:
                mapb[cnt] = 1
        
        acnt, bcnt = 0, 0
        
        for key in mapa:
            if key > 2:
                acnt += (key-2)*mapa[key]
                
        for key in mapb:
            if key > 2:
                bcnt += (key-2)*mapb[key]
                
        return acnt > bcnt