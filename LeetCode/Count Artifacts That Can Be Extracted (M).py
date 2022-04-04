class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        site = [ [0]*n for i in range(n) ]
                    
        for d in dig:
            a, b = d[0], d[1]
            site[a][b] = 1
        
        ctr = 0
        for art in artifacts:
            a, b, c, d = art[0], art[1], art[2], art[3]
            flag = 1
            for i in range(a, c+1):
                for j in range(b, d+1):
                    if site[i][j] == 0: 
                        flag = 0
                        break
            if flag: ctr += 1
                
        return ctr