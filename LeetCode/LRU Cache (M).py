class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.prev = dict()
        self.next = dict()
        self.tail = '#'
        self.head = '$'
        self.connect(self.head, self.tail)
        
    def connect(self, a, b):
        self.prev[b] = a
        self.next[a] = b
        
    def delete(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.cache[key], self.prev[key], self.next[key]

    def append(self, key, value):
        self.cache[key] = value
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)
        self.append(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)