def answer(l):
    #O(n^2)
    
    sol = 0
    pl = [0]*len(l)
    for x in range(len(l)):
        for y in range(x+1, len(l)):
            if l[y] % l[x] == 0:
                pl[y] += 1
                
                if pl[x] > 0:
                    sol += pl[x]
    
    return sol

def test():
    # Provided test cases.
    assert(answer([1, 1, 1]) == 1)
    assert(answer([1, 2, 3, 4, 5, 6]) == 3)

    # Custom test cases.
    assert(answer([1]) == 0)
    assert(answer([1, 2]) == 0)
    assert(answer([2, 4]) == 0)
    assert(answer([1, 1, 1, 1]) == 4)
    assert(answer([1, 1, 1, 1, 1]) == 10)
    assert(answer([1, 1, 1, 1, 1, 1]) == 20)
    assert(answer([1, 1, 1, 1, 1, 1, 1]) == 35)
    assert(answer([1, 1, 2]) == 1)
    assert(answer([1, 1, 2, 2]) == 4)
    assert(answer([1, 1, 2, 2, 2]) == 10)
    assert(answer([1, 1, 2, 2, 2, 3]) == 11)
    assert(answer([1, 2, 4, 8, 16]) == 10)
    assert(answer([2, 4, 5, 9, 12, 34, 45]) == 1)
    assert(answer([2, 2, 2, 2, 4, 4, 5, 6, 8, 8, 8]) == 90)
    assert(answer([2, 4, 8]) == 1)
    assert(answer([2, 4, 8, 16]) == 4)
    assert(answer([3, 4, 2, 7]) == 0)
    assert(answer([6, 5, 4, 3, 2, 1]) == 0)
    assert(answer([4, 7, 14]) == 0)
    assert(answer([4, 21, 7, 14, 8, 56, 56, 42]) == 9)
    assert(answer([4, 21, 7, 14, 56, 8, 56, 4, 42]) == 7)
    assert(answer([4, 7, 14, 8, 21, 56, 42]) == 4)

    print("ok!")


test()
