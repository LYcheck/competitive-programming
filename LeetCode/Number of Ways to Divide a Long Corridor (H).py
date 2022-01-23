class Solution:
    def numberOfWays(self, corridor: str) -> int:
        chaircnt, flag, cnt = 0, 0, 0
        res = 1

        for item in corridor:
            if item == 'S': chaircnt += 1
            
            if chaircnt != 0 and not chaircnt%2: flag = 1
            else:
                if cnt: res = (res*cnt)%(10**9+7)
                flag = 0
            
            if flag: cnt += 1
            else: cnt = 0
                
        #if chaircnt & 1: return 0
        return res if chaircnt > 1 and not chaircnt&1 else 0