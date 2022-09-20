class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def dfs(temp):
            if len(str(temp)) == n:
                nonlocal res
                res += [temp]
                return
            
            c1 = temp%10
            if c1+k <= 9: dfs(temp*10 + c1+k)
            if k != 0 and c1-k >= 0: dfs(temp*10 + c1-k)
                
        for i in range(1, 10):
            dfs(i)
            
        return res