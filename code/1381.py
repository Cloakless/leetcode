class CustomStack:

    def __init__(self, maxSize: int):
        self.data = [0] * maxSize
        self.n = 0
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if self.n < self.max_size:
            self.data[self.n] = x
            self.n += 1
        

    def pop(self) -> int:
        if self.n == 0:
            return -1
        self.n -= 1
        return self.data[self.n]
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.n)):
            self.data[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
