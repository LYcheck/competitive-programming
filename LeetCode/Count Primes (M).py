class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        
        ctr = n-2
        prime = [1]*n
        
        prime[0], prime[1] = 0, 0
        for i in range(2, ceil(sqrt(n))):
            if prime[i]:
                for j in range(i*i, n, i):
                    if prime[j]:
                        prime[j] = 0
                        ctr -= 1
        return ctr