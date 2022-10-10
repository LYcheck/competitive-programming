class MyCalendarThree:
    def __init__(self):
        self.segtree = collections.defaultdict(int)
        self.lazyprop = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        def update(s, e, l=0, r=10**9, node=1):
            #boundcheck
            if r <= s or l >= e: return
            #valid
            if s <= l < r <= e: 
                self.segtree[node] += 1
                self.lazyprop[node] += 1
            else:
                m = (l+r)//2
                update(s, e, l, m, node*2)
                update(s, e, m, r, node*2+1)
                self.segtree[node] = self.lazyprop[node] + max(self.segtree[node*2], \
                                                               self.segtree[node*2+1])
        
        update(start, end)
        return self.segtree[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)