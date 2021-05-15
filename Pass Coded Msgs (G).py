from itertools import combinations 

def solution(l):
    # Your code here
    # 3div rule, sum of digits must be divisible by 3
    # combinations() returns (1,2) (1,3) (1,4) (2,3) etc
    
    l.sort(reverse=True)
    
    for x in range(len(l), 0, -1):
        for thing in combinations(l, x):
            if sum(thing)%3 == 0:
                s = ''.join(map(str, thing))
                return int(s)

    return 0
