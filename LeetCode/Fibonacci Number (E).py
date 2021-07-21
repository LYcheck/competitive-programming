class Solution:
    def fib(self, n: int) -> int:
        fib = [1]*n
        if n < 2:
            if not n:
                return 0
            return 1
        
        for _ in range(2,n):
            fib[_] = fib[_-1] + fib[_-2]
        
        return fib[-1]
