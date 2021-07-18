def solution(n):
    n = int(n)
    if n == 0: return 1
    
    ans = 0
    while(n != 1):
        if not n & 1:
            n = n>>1
        else:
            #if bin(n+1).count("1") > bin(n-1).count("1"):
            if (((n+1)&n) > ((n-1)&(n-2)) or n==3):
                n -= 1
            else:
                n += 1
        
        ans += 1
        
    return ans
