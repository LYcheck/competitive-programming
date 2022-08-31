class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        fromleft = [0]*n
        fromright = [0]*n
        
        for i in range(1,n):
            if security[i] <= security[i-1]: fromleft[i] = fromleft[i-1]+1
            if security[~i] <= security[~i+1]: fromright[~i] = fromright[~i+1]+1
        
        res = []
        for i in range(n):
            if fromleft[i] >= time and fromright[i] >= time: res += [i]
                
        return res
        # print(security)
        # print(fromleft)
        # print(fromright)