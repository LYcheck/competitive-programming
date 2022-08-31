class MedianFinder:

    def __init__(self):
        self.left = [] #maxheap
        self.right = [] #minheap

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            #pop from right, push popped to left, add to right
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))
        else:
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] -self.left[0]) / 2.0
        else:
            return self.right[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()