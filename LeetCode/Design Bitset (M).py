class Bitset:

    def __init__(self, size: int):
        self.bitset = 0
        self.size = size
        self.cnt = 0

    def fix(self, idx: int) -> None:
        if not self.bitset & (1 << idx):
            self.bitset |= (1 << idx)
            self.cnt += 1

    def unfix(self, idx: int) -> None:
        if self.bitset & (1 << idx) == 1 << idx:
            self.bitset ^= 1 << idx
            self.cnt -= 1

    def flip(self) -> None:
        self.bitset ^= ((1 << self.size)-1)
        self.cnt = self.size - self.cnt

    def all(self) -> bool:
        return self.size == self.cnt

    def one(self) -> bool:
        return self.bitset > 0

    def count(self) -> int:
        return self.cnt
    
    def toString(self) -> str:
        temp = bin(self.bitset)[2:]
        return temp[::-1] + "0"*(self.size-len(temp))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()