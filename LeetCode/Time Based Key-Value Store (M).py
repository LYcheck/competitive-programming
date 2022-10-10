class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store: self.store[key] += [[timestamp, value]]
        else: self.store[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or len(self.store[key]) == 0: return ""
        idx = bisect.bisect_left(self.store[key], timestamp, key=lambda x:x[0])
        if idx < len(self.store[key]): 
            if self.store[key][idx][0] > timestamp: 
                if idx == 0: return ""
                else: return self.store[key][idx-1][1]
            return self.store[key][idx][1]
        else: return self.store[key][-1][1]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)