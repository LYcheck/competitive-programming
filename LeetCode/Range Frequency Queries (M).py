class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.map = dict()
        
        for i in range(len(arr)):
            val = arr[i]
            if val in self.map:
                self.map[val] += [i]
            else:
                self.map[val] = [i]

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.map:
            return 0
        else:
            slist = self.map[value]
            maxi = bisect.bisect_right(slist, right)
            mini = bisect.bisect_left(slist, left)
            
            return maxi-mini


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)