class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        
        for p in points:
            temp = {}
            for q in points:
                t1 = p[0]-q[0]
                t2 = p[1]-q[1]
                tt = t1**2 + t2**2
                
                if tt in temp: temp[tt] += 1
                else: temp[tt] = 1
                    
            for k in temp.keys():
                res += temp[k]*(temp[k]-1)
                
        return res