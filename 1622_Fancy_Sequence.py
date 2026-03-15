class Fancy:
    def __init__(self):
        self.arr = []
        self.a = 0
        self.b = 1
        self.mod = 10 ** 9 + 7

    def append(self, val: int) -> None:
        self.arr.append((val-self.a) * pow(self.b, self.mod-2, self.mod) % self.mod)

    def addAll(self, inc: int) -> None:
        self.a = (self.a + inc) % self.mod
    def multAll(self, m: int) -> None:
        self.a = (self.a * m)  % self.mod
        self.b = (self.b * m) % self.mod
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        else:
            return ((self.arr[idx] * self.b) + self.a) % self.mod

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)