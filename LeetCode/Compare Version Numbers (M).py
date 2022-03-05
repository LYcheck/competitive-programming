class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1 = len(v1)
        n2 = len(v2)
        v1 = [ int(x) for x in v1 ]
        v2 = [ int(x) for x in v2 ]
        
        for i in range(max(n1, n2)):
            if i >= n1:
                if v2[i] != 0: return -1
                continue

            elif i >= n2:
                if v1[i] != 0: return 1
                continue
            
            else:
                if v1[i] > v2[i]: return 1
                elif v1[i] < v2[i]: return -1
                
        return 0