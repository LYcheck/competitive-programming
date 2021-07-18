def getParent(h, n):
    nmax = 2**h-1
    if n > nmax-1: return -1

    prenum = 0
    while True:
        nmax = nmax // 2

        left = prenum + nmax
        right = left + nmax
        node = right+1

        if left == n or right == n:
            return node

        if n > left:
            prenum = left

def solution(h, q):
    ans = list()

    for x in q:
        ans.append(getParent(h, x))

    return ans

print(solution(3, [1,3,7]))
