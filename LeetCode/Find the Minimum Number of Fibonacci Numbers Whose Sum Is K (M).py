class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [0]*500
        fib[0] = 1
        fib[1] = 1
        
        ptr = 2
        while 1:
            fib[ptr] = fib[ptr-1] + fib[ptr-2]
            if fib[ptr] >= k: break
            ptr += 1
        
        if fib[ptr] > k: ptr -= 1
    
        res = 0
        while ptr > -1 and k > 0:
            if fib[ptr] <= k:
                res += 1
                k -= fib[ptr]
            ptr -= 1
            
        return res