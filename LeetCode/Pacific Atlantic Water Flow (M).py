class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlseen, pacseen = {}, {}
        rows, cols = len(heights), len(heights[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        q, res = [], []
        
        for i in range(cols): q += [(0, i)]
        for i in range(1, rows): q += [(i, 0)]
            
        print(q)
            
        while q:
            cur = q[0]
            q.pop(0)
            crow, ccol = cur
            if (crow, ccol) not in pacseen: pacseen[crow, ccol] = 1
            
            for drow, dcol in dirs:
                nrow = crow + drow
                ncol = ccol + dcol
                if (nrow, ncol) in pacseen: continue
                if 0<=nrow<rows and 0<=ncol<cols:
                    if heights[nrow][ncol] >= heights[crow][ccol]:
                        pacseen[nrow, ncol] = 1
                        q += [(nrow, ncol)]
        
        for i in range(cols): q += [(rows-1, i)]
        for i in range(rows-1): q += [(i, cols-1)]
        
        print(q)
            
        while q:
            cur = q[0]
            q.pop(0)
            crow, ccol = cur
            if (crow, ccol) in pacseen and (crow, ccol) not in atlseen: res += [[crow, ccol]]
            atlseen[crow, ccol] = 1
            
            for drow, dcol in dirs:
                nrow = crow + drow
                ncol = ccol + dcol
                if (nrow, ncol) in atlseen: continue
                if 0<=nrow<rows and 0<=ncol<cols:
                    if heights[nrow][ncol] >= heights[crow][ccol]:
                        q += [(nrow, ncol)]
                        
        return sorted(res)
                        